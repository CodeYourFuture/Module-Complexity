class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = DLLNode(None, None)
        self.tail = DLLNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_front(self, node):
        self.remove(node)
        self.add_to_front(node)

    def remove_last(self):
        if self.tail.prev is self.head:
            return None
        last = self.tail.prev
        self.remove(last)
        return last


class LruCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoublyLinkedList()

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.list.move_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.list.move_to_front(node)
            return

        new_node = DLLNode(key, value)
        self.cache[key] = new_node
        self.list.add_to_front(new_node)

        if len(self.cache) > self.capacity:
            last = self.list.remove_last()
            del self.cache[last.key]
