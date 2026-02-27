class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _add_to_head(self, node):
        """Put node at the front (most recently used)."""
        node.previous = None
        node.next = self.head

        if self.head is not None:
            self.head.previous = node
        self.head = node

        if self.tail is None:
            # First node in the list
            self.tail = node

    def _remove_node(self, node):
        """Detach node from the linked list."""
        prev = node.previous
        nxt = node.next

        if prev is not None:
            prev.next = nxt
        else:
            # node was head
            self.head = nxt

        if nxt is not None:
            nxt.previous = prev
        else:
            # node was tail
            self.tail = prev

        node.next = None
        node.previous = None

    def _move_to_head(self, node):
        """Mark node as most recently used."""
        if node is self.head:
            return
        self._remove_node(node)
        self._add_to_head(node)

    # ---- public API ----
class LruCache:
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

        # mark as recently used
        self._move_to_head(node)
        return node.value

    def set(self, key, value):
        node = self.map.get(key)

        if node is not None:
            # update existing
            node.value = value
            self._move_to_head(node)
            return

        # new key
        if len(self.map) >= self.limit:
            # evict least recently used (tail)
            lru = self.tail
            if lru is not None:
                self._remove_node(lru)
                del self.map[lru.key]

        new_node = _Node(key, value)
        self._add_to_head(new_node)
        self.map[key] = new_node
