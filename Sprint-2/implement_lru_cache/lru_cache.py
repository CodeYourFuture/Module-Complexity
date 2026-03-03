from collections import OrderedDict

class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be positive")

        self.limit = limit
<<<<<<< HEAD
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
=======
        self.cache = OrderedDict()
>>>>>>> fc65c37 (lru cache update)

    def get(self, key):
        if key not in self.cache:
            return None

        # Move key to the end (most recently used)
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        if key in self.cache:
            # Update existing and move to end
            self.cache.pop(key)

        elif len(self.cache) >= self.limit:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)

        # Insert as most recently used
        self.cache[key] = value