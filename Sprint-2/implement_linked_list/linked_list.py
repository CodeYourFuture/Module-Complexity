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
        new_node = Node(value)

        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node

        self.head = new_node
        return new_node

    def pop_tail(self):
        if self.tail is None:
            return None

        removed = self.tail

        if self.tail.previous:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.head = None
            self.tail = None

        return removed.value

    def remove(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next
            if self.head:
                self.head.previous = None

        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous