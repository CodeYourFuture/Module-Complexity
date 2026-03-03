class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        #first 
        self.head = None
        #last
        self.tail = None

    def push_head(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        return new_node

    def pop_tail(self):
        if self.tail is None:
            return None

        removed = self.tail
        value = removed.value

        self.remove(removed)

        return value

    def remove(self, node):
        if node is None:
            return

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.previous

        if node.previous:
            node.previous.next = node.next

        if node.next:
            node.next.previous = node.previous

        node.next = None
        node.previous = None