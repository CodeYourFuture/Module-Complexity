class Node:
    __slots__ = ("value", "previous", "next")

    def __init__(self, value):
        self.value = value
        self.previous: "Node | None" = None
        self.next: "Node | None" = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def push_head(self, value) -> Node:
        """Add a value to the front of the list. Returns a handle for O(1) removal."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        return node

    def pop_tail(self):
        """Remove and return the value at the end of the list."""
        if self.tail is None:
            raise IndexError("pop from empty list")
        node = self.tail
        self.remove(node)
        return node.value

    def remove(self, node: Node) -> None:
        """Remove a node from the list in O(1) using a handle from push_head"""
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous = None
        node.next = None
