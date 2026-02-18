#Implementing a doubly linked list to reduce complexity of each operation which was previously O(n) to O(1).
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # MRU
        self.tail = None  # LRU

    def push_head(self, node): #accessing or adding a new key at head- MRU
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node
        self.head = node

        if self.tail is None:
            self.tail = node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next #previous node connects to the next node.
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def pop_tail(self): #removes to return lru node
        if self.tail is None:
            return None
        node = self.tail
        self.remove(node)
        return node



class LruCache:
    def __init__(self,limit) -> None:
        if limit <= 0:           
            raise ValueError("Limit must be greater than zero")
        self.limit = limit #defines a limit, after which before adding anything in our cache we need to remove it
        self.storage = {} #key(cachekey) and node(key value pair)
        self.order = DoublyLinkedList() #self.head is MRU and self.tail is LRU
        pass

#If a key already exists move it to MRU position
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
       

    def get(self,key):
            if key not in self.storage:
                return None
            node = self.storage[key]
            self.touch(node)
            return node.value
    
