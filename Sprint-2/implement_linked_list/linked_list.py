class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None  # renamed from prev
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        """Add element to start (O(1))"""
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.previous = new_node
        else:
            # If list was empty, tail is also the new node
            self.tail = new_node

        self.head = new_node
        return new_node  # handle for later removal

    def pop_tail(self):
        """Remove element from end (O(1))"""
        if not self.tail:
            raise IndexError("pop_tail from empty list")

        value = self.tail.value
        self.remove(self.tail)
        return value

    def remove(self, node):
        """Remove node (O(1)) using the handle"""
        if node.previous:
            node.previous.next = node.next
        else:
            # Node is head
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            # Node is tail
            self.tail = node.previous

        node.previous = node.next = None 
