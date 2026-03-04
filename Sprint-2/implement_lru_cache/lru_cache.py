
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value      
        self.previous = None        
        self.next = None       
class LinkedList:
    def __init__(self):
        self.head = None        
        self.tail = None        

    # adding a new value in the front of the list
    def push_head(self, node):
        node.previous = None
        node.next = self.head      

        if self.head is None:   # if list is empty head and tail becomes this node.
            self.head = node    
            self.tail = node    
        else:
            self.head.previous = node   
            self.head = node        

        return node  # returns the node so we can remove it later
    
    # removing last element
    def pop_tail(self):
        if self.tail is None:   
            raise Exception("List is empty")

        removed = self.tail 
        self.remove(removed)
        return removed

    # removes a specific node 
    def remove(self, node):

        if node.previous is None:   # if removing head
            self.head = node.next
        else:
            node.previous.next = node.next  # connect previous to next

        if node.next is None:   # if removing tail
            self.tail = node.previous
        else:
            node.next.previous = node.previous  # connect next to previous
    # unplugging node
        node.next = None
        node.previous = None

class LruCache:
    def __init__(self,limit) -> None:
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")
        self.limit = limit

        self.storage =  {} 
        self.order = LinkedList()
        pass

    #If key already exists move it to MRU
    def touch (self,node):
        self.order.remove(node)
        self.order.push_head(node)
    
    # If we want to add or update a key value pair
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]   #update the value of the key 
            node.value = value
            self.touch(node)
            return
        
        #if we are adding a new key and at our limit 
        if len(self.storage) >= self.limit:
            lru_node =self.order.pop_tail()
            del self.storage[lru_node.key]

        #insert a new node
        new_node = Node(key, value)
        self.order.push_head(new_node)
        self.storage[key] = new_node
       
    # updating position to most recently used 
    def get(self,key):
        if key not in self.storage:
            return None
        node = self.storage[key]
        self.touch(node)
        return node.value