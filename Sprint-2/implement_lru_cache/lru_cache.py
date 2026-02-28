class _Node:
    def __init__(self, value):
        self.value = value  # stores as (key, value) tuple
        self.next = None
        self.previous = None


class DoublyLinkedList:
    """responsible only for managing a doubly linked list.
    stores values as (key, value) tuples but knows nothing about cachin
    """
    def __init__(self):
        self.head = None  # most recently used end
        self.tail = None  # least recently used end

    def add_to_head(self, value):
        """sreates a new node with value, add to head, returns the node."""
        node = _Node(value)
        node.next = self.head
        node.previous = None
        if self.head is not None:
            self.head.previous = node
        self.head = node
        if self.tail is None:
            self.tail = node
        return node

    def remove_node(self, node):
        """detaches any node from the list."""
        prev = node.previous
        nxt = node.next
        if prev is not None:
            prev.next = nxt
        else:
            self.head = nxt
        if nxt is not None:
            nxt.previous = prev
        else:
            self.tail = prev
        node.next = None
        node.previous = None

    def remove_tail(self):
        """removes and returns the tail node """
        lru = self.tail
        if lru is not None:
            self.remove_node(lru)
        return lru


class LruCache:
    """responsible only for cache logic (get, set, eviction).
   gives all all ordering to DoublyLinkedList.
    """
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be positive")
        self.limit = limit
        self.map = {}                    
        self.list = DoublyLinkedList()   

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return None
        # re-inserts at head to mark as most recently used
        self.list.remove_node(node)
        new_node = self.list.add_to_head(node.value)
        self.map[key] = new_node         # updates map to point to new node
        return new_node.value[1]         

    def set(self, key, value):
        node = self.map.get(key)
        if node is not None:
            # key exists then remove old, adds updated to head
            self.list.remove_node(node)
            new_node = self.list.add_to_head((key, value))
            self.map[key] = new_node     # update map to new node
            return
        # new key gets rid of LRU 
        if len(self.map) >= self.limit:
            lru = self.list.remove_tail()
            if lru is not None:
                del self.map[lru.value[0]]  
        new_node = self.list.add_to_head((key, value))
        self.map[key] = new_node        
        new_node = _Node(key, value)
        self._add_to_head(new_node)
        self.map[key] = new_node
