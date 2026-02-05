class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.previous = node
        self.head = node
        if self.tail is None:
            self.tail = node
        return node

    def pop_tail(self):
        if self.tail is None:
            return None
        node = self.tail
        value = node.value
        if node.previous:
            self.tail = node.previous
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return value

    def remove(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous
        node.next = None
        node.previous = None
