class Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LruCache:
    def __init__(self, limit: int):
        if limit < 1:
            raise ValueError(f"limit must be at least 1, got {limit}")

        self._limit = limit
        self.map: dict = {}
        self.head = None
        self.tail = None

    def _remove_node(self, node: Node):
        """Remove a node from the linked list in O(1) time."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        node.prev = None
        node.next = None

    def _add_node_to_head(self, node: Node):
        """Add a node to the head of the linked list in O(1) time."""
        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        
        self.head = node

    def get(self, key):
        """Return the value for key, Non if not present"""
        node = self.map.get(key)
        if node is None:
            return None
        
        self._touch(node)
        return node.value

    def set(self, key, value) -> None:
        """Combine value with key, evicting the LRU entry if necessary."""
        node = self.map.get(key)

        if node:
            node.value = value
            self._touch(node)
        else:
            if len(self.map) >= self._limit:
                self._evict()
            
            new_node = Node(key, value)
            self._add_node_to_head(new_node)
            self.map[key] = new_node

    def _touch(self, node) -> None:
        """Move an existing node to the head (most-recently-used position)."""
        self._remove_node(node)
        self._add_node_to_head(node)

    def _evict(self) -> None:
        """Remove the least-recently-used entry (tail of the list)."""
        if self.tail is None:
            return
        
        lru = self.tail
        self._remove_node(lru)
        del self.map[lru.key]
