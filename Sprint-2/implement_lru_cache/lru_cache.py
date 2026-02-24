class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be positive")

        self.limit = limit
        self.cache = {}  # key -> node
        self.head = None  # Most recently used
        self.tail = None  # Least recently used

    # ---------------------
    # Internal helpers
    # ---------------------

    def _remove_node(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous = None
        node.next = None

    def _add_to_head(self, node):
        node.next = self.head
        node.previous = None

        if self.head:
            self.head.previous = node
        else:
            self.tail = node

        self.head = node

    # ---------------------
    # Public API
    # ---------------------

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return None

        # Move to head (recently used)
        self._remove_node(node)
        self._add_to_head(node)

        return node.value

    def set(self, key, value):
        node = self.cache.get(key)

        if node:
            # Update value and move to head
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
            return

        # If full, evict LRU (tail)
        if len(self.cache) >= self.limit:
            lru = self.tail
            self._remove_node(lru)
            del self.cache[lru.key]

        # Insert new node
        new_node = Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node
