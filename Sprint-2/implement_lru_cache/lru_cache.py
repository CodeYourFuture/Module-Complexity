class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None   # point to previous node
        self.next = None  # point to next node


class LruCache:
    def __init__(self,limit):
        self.limit = limit
        self.cache = {}  # for store node objects

        #dummy nodes for making insert and remove easier
        self.head = Node(None,None)
        self.tail = Node(None,None)

        #linking two dummy nodes
        self.head.next = self.tail
        self.tail.prev =  self.head

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self,node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def move_to_front (self,node):
        self.remove(node)
        self.add_to_front(node)

    def get (self,key):
        if key not in self.cache:
            return None
        
        node = self.cache[key]
        self.move_to_front(node)
        return node.value
    
    def set(self,key,value):
        if self.limit <= 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)
            return
        if len(self.cache) >= self.limit:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]

            new_node = Node(key,value)
            self.cache[key] = new_node
            self.add_to_front(new_node)
        




