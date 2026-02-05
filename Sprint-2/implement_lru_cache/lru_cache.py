class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than zero")

        self.limit = limit
        self.cache = {}
        self.head = None    
        self.tail = None
        self.size = 0

    
    #to remove a node frpm linkedlist
    def _remove_node(self, node: Node): 
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = node.next = None


    #Add a node to the head of the linked list
    def _add_to_head(self, node: Node):
        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node
        self.head = node

        if not self.tail:
            self.tail = node  


    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        # Move node to head (most recently used)
        self._remove_node(node)
        self._add_to_head(node)
        return node.value


    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1

            if self.size > self.limit:
                # Evict LRU (tail node)
                lru = self.tail
                self._remove_node(lru)
                del self.cache[lru.key]
                self.size -= 1                          
