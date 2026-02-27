class Node:
    """Represents a node in the doubly-linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    """Manages insertion, removal, and reordering of nodes in a doubly-linked list."""
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, node):
        """Add a node to the head of the list."""
        node.next = None
        node.previous = None
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
    
    def move_to_head(self, node):
        """Move an existing node to the head of the list."""
        if node == self.head:
            return
        
        self.remove_node(node)
        self.add_to_head(node)
    
    def remove_node(self, node):
        """Remove a node from the list."""
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
    
    def get_tail(self):
        """Return the tail node (least recently used)."""
        return self.tail


class LruCache:
    """Implements an LRU cache with O(1) operations."""
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than 0")
        
        self.limit = limit
        self.cache = {}  
        self.order = DoublyLinkedList()
    
    def get(self, key):
        """Retrieve a value and mark it as recently used."""
        if key not in self.cache:
            return None
        
        node = self.cache[key]
        self.order.move_to_head(node)
        
        return node.value
    
    def set(self, key, value):
        """Store a key-value pair and evict LRU if necessary."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.order.move_to_head(node)
        else:
            if len(self.cache) >= self.limit:
                self._evict_lru()
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.order.add_to_head(new_node)
    
    def _evict_lru(self):
        """Remove the least recently used item."""
        lru_node = self.order.get_tail()
        if lru_node is not None:
            del self.cache[lru_node.key]
            self.order.remove_node(lru_node)
