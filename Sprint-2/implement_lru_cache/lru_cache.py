class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def pop_tail(self):
        if not self.tail:
            return None
        old_tail=self.tail
        self.remove(old_tail)
        return old_tail

class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("limit must be > 0")

        self.limit = limit
        self.cache = {}
        self.list = List()

    def set(self, key, value):
        node = self.cache.get(key)

        if node:
            node.value=value
            self.list.move_to_head(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.list.add_to_head(node)

        if len(self.cache) >= self.limit:
            tail=self.list.pop_tail()
            if tail:
                del self.cache[tail.key]

    def get(self, key):
        node = self.cache.get(key)

        if node is None:
            return None
        else:
            self.list.move_to_head(node)
            return node.value
