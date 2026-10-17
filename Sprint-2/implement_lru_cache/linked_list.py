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
        node = Node(value)
        node.next = self.head

        if self.head is None:
            self.tail = node
        else:
            self.head.previous = node

        self.head = node
        return node

    def pop_tail(self):
        if self.tail is None:
            return None

        node = self.tail
        self.remove(node)
        return node.value

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
