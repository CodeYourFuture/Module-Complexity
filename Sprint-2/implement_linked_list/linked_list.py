class ListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        new_node = ListNode(value)
        new_node.next = self.head

        if self.head:
            self.head.previous = new_node

        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        return new_node
