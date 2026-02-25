class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than 0")
        
        self.limit = limit
        self.cache = {}  
        self.head = None  
        self.tail = None  
    
    def get(self, key):
        if key not in self.cache:
            return None
        
        node = self.cache[key]
        
        self._move_to_head(node)
        
        return node.value
    
    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.limit:
                self._evict_tail()
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
    
    def _move_to_head(self, node):
        if node == self.head:
            return
        
        self._remove_node(node)
        
        self._add_to_head(node)
    
    def _remove_node(self, node):
        if node == self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.previous = None
        elif node == self.tail:
            self.tail = node.previous
            self.tail.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
        
        node.next = None
        node.previous = None
    
    def _add_to_head(self, node):
        node.next = None
        node.previous = None
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
    
    def _evict_tail(self):
        if self.tail is None:
            return
        
        del self.cache[self.tail.key]
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
