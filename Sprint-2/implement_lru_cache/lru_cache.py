#a node class is created with key,value... key is used to evict a specific char
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

#next step i define helper functions to add and remove node : 
#I use the same concept of the previous project of the linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail #this is most recently used
        self.tail.previous = self.head  #this is the least recently used

    def add_to_head(self, node):
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.previous
        nxt = node.next
        prev.next = nxt
        nxt.previous = prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def pop_tail(self):
        node = self.tail.previous
        self.remove_node(node)
        return node
    

#Lru class for the logic
class LruCache:
    def __init__(self, limit):     #constructing 
        if limit <= 0:
            raise ValueError("Cache limit must be greater than zero") #b/c it is not logical to have a cache with negative or 0 capacity
        self.limit = limit  #to tell the limit of our cache
        self.cache = {}  #empty cache with key->node
        self.dll = DoublyLinkedList() #i set the helper method as dll 
    def get(self, key):   #Retrieve value and mark as recently used
        node = self.cache.get(key)
        if not node:
            return None
        # Move the node to the head (most recently used)
        self.dll.move_to_head(node)
        return node.value
    def set(self, key, value): #Insert/update value and handle eviction
        node = self.cache.get(key)
        if node:
            #Update existing node and move it to head
            node.value = value
            self.dll.move_to_head(node)
        else:
            #Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.dll.add_to_head(new_node)
            if len(self.cache) > self.limit:
                # Remove least recently used node
                tail = self.dll.pop_tail()
                del self.cache[tail.key]
#Time Complexity = O(1) since each operations have the same O(1) complexity
#Total Space complexity is O(n) i.e. One node and one dictionary entry per cached item
