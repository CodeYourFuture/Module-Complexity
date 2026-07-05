class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")

        self.limit = limit
        self.cache = {}
        self.head = None
        self.tail = None

    def _add_to_head(self, node):
        node.previous = None
        node.next = self.head

        if self.head is not None:
            self.head.previous = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def _move_to_head(self, node):
        if node == self.head:
            return

        if node.previous is not None:
            node.previous.next = node.next

        if node.next is not None:
            node.next.previous = node.previous

        if node == self.tail:
            self.tail = node.previous

        node.previous = None
        node.next = self.head

        if self.head is not None:
            self.head.previous = node

        self.head = node

    def _remove_tail(self):
        if self.tail is None:
            return

        old_tail = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.previous
            self.tail.next = None

        del self.cache[old_tail.key]

    def get(self, key):
        node = self.cache.get(key)

        if node is None:
            return None

        self._move_to_head(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return

        node = Node(key, value)

        self.cache[key] = node
        self._add_to_head(node)

        if len(self.cache) > self.limit:
            self._remove_tail()