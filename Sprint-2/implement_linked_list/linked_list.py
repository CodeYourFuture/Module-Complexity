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
        """Insert a new node at the head and return the node."""
        new_node = Node(value)

        if self.head is None:
            # Empty list: head and tail are the same node
            self.head = new_node
            self.tail = new_node
        else:
            # Non‑empty: link new node before current head
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        return new_node

    def pop_tail(self):
        """Remove the tail node and return its value."""
        if self.tail is None:
            raise IndexError("pop from empty linked list")

        node = self.tail
        value = node.value
        self.remove(node)
        return value

    def remove(self, node):
        """Remove an arbitrary node from the list."""
        if node is None:
            return

        # Fix previous node's next pointer
        if node.previous is not None:
            node.previous.next = node.next
        else:
            # node was head
            self.head = node.next

        # Fix next node's previous pointer
        if node.next is not None:
            node.next.previous = node.previous
        else:
            # node was tail
            self.tail = node.previous

        # Detach removed node
        node.next = None
        node.previous = None
