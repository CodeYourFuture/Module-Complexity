class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("limit must be > 0")

        self.head = None
        self.tail = None
        self.limit = limit
        self.dict = {}

    def set(self, key, value):
        node = Node(key, value)

        self.dict[key] = node
        self.add_to_head(node)

        if len(self.dict) > self.limit:
            self.evict_tail()


    def get(self, key):
        node = self.dict.get(key)

        if node is None:
            return None
        else:
            self.move_to_head(node)
            return node.value

    def add_to_head(self, node):
        node.previous = None
        node.next = self.head

        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.previous = node
            self.head = node

    def remove(self, node):
        if node.previous is None:
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:
            self.tail = node.previous
        else:
            node.next.previous = node.previous

        node.previous = None
        node.next = None

    def move_to_head(self, node):
        if node is self.head:
            return
        self.remove(node)
        self.add_to_head(node)

    def evict_tail(self):
        if self.tail is None:
            return

        old_tail = self.tail
        self.remove(old_tail)
        del self.dict[old_tail.key]