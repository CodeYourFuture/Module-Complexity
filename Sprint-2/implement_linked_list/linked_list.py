class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        new_node = Node(value)  # <-- Node must exist
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        return new_node

    def pop_tail(self):
        if not self.tail:
            return None
        old_tail = self.tail
        value = old_tail.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = old_tail.previous
            self.tail.next = None

        old_tail.previous = None
        old_tail.next = None  

        return value

    def remove(self, node):
        if node is self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None

        if node is self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None

        if node.previous:
            node.previous.next = node.next

        if node.next:
            node.next.previous = node.previous

        node.previous = node.next = None

