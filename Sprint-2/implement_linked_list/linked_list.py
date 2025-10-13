class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, element):
        node = Node(element)
        if self.head and self.tail:
            node.next = self.head
            self.head.previous = node
            self.head = node
        elif not self.head and not self.tail:
            self.head = node
            self.tail = node
        return node

    def pop_tail(self):
        node = self.tail
        if self.tail is not self.head:
            self.tail = node.previous
            node.previous.next = None
            node.previous = None
        else:
            self.head = None
            self.tail = None
        return node.value

    def remove(self, node):
        if self.head != node and self.tail != node:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.previous, node.next = None, None
        elif self.head == node and self.tail != node:
            node.next.previous = None
            self.head = node.next
            node.previous, node.next = None, None
        elif self.head != node and self.tail == node:
            node.previous.next = None
            self.tail = node.previous
            node.previous, node.next = None, None
        elif self.head == node and self.tail == node:
            self.head = None
            self.tail = None


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
