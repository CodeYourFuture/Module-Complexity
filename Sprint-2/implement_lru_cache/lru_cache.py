class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = limit
        self.cache = {}

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
