class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, element):
        node = Node(element)
        if self.head:
            node.next = self.head
            self.head.previous = self.head = node
        else:
            self.head = node
            self.tail = node
        return node

    def pop_tail(self):
        # get current tail
        node = self.tail
        if self.tail is not self.head:
            # replace the tail
            self.tail = node.previous
            # reset to none
            self.tail.next = node.previous = None
        else:
            self.head = None
            self.tail = None
        return node.value

    def remove(self, node):
        if self.head == node:
            if self.tail == node:
                # head == node, tail == node
                self.head = self.tail = None
            else:
                # head == node, tail != node
                self.head = node.next
                node.next.previous = node.previous = node.next = None
        else:
            if self.tail == node:
                # head != node, tail == node
                self.tail = node.previous
                self.tail.next = node.previous = None
            else:
                # head != node, tail != node
                node.previous.next = node.next
                node.next.previous = node.previous
                node.previous = node.next = None


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
