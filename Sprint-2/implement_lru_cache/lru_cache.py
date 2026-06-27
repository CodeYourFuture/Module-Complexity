class CacheNode:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.previous = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value) -> Node:
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            
        return new_node

    def remove(self, node: Node) -> None:
        if node is None:
            return

        if node == self.head:
            self.head = node.next
            
        if node == self.tail:
            self.tail = node.previous

        if node.previous is not None:
            node.previous.next = node.next
            
        if node.next is not None:
            node.next.previous = node.previous

        node.next = None
        node.previous = None

    def pop_tail(self):
        if self.tail is None:
            return None
        
        last_node = self.tail
        value = last_node.value
        
        self.remove(last_node)
        
        return value        

class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than 0")
        
        self.limit = limit
        self.lookup = {}
        self.head = None 
        self.tail = None   

    def _remove_node(self, node: CacheNode):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.previous

        if node.previous is not None:
            node.previous.next = node.next
        if node.next is not None:
            node.next.previous = node.previous

        node.next = None
        node.previous = None

    def _move_to_head(self, node: CacheNode):
        node.next = self.head
        node.previous = None
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            self.head = node

    def get(self, key):
        if key not in self.lookup:
            return None
            
        node = self.lookup[key]
        self._remove_node(node)
        self._move_to_head(node)
        return node.value

    def set(self, key, value) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.value = value
            self._remove_node(node)
            self._move_to_head(node)
        else:
            new_node = CacheNode(key, value)
            
            if len(self.lookup) >= self.limit:
                oldest_node = self.tail
                if oldest_node is not None:
                    del self.lookup[oldest_node.key]  
                    self._remove_node(oldest_node)    
            
            self._move_to_head(new_node)
            self.lookup[key] = new_node