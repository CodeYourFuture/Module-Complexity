class Node:
    """
    A node in a double linked list.

    Each node supports a data, previous, and next
    - data: the value
    - previous: pointer to the previous node
    - next: pointer to the next node
    """

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class LinkedList:
    """
    Double Linked List

    Supports O(1) operations on insertion at head, removal from tail, and removal from arbitrary node
    """
    def __init__(self):
        # Head points to the first node in the list
        self.head = None
        
        # Tail points to the last node in the list
        self.tail = None

    def is_empty(self):
        """Returns True if the list contains no nodes."""
        return self.head is None

    def push_head(self, data):
        """
        Insert a new node at the head of the list.

        Time Complexity: O(1)

        Returns:
            Node: reference to the inserted node (handle for later removal)
        """
        node = Node(data)

        if self.is_empty():
            # If list is empty, head and tail both point to new node
            self.head = node
            self.tail = node
        else:
            # Link new node before current head
            node.next = self.head
            self.head.previous = node

            # Update head pointer
            self.head = node

        return node

    def pop_tail(self):
        """
        Remove and return the value at the tail of the list.

        Time Complexity: O(1)

        Raises:
            ValueError: if the list is empty
        """

        if self.is_empty():
            raise ValueError("List is empty.")
        
        # store value before removing node
        value = self.tail.data

        if self.head == self.tail:
            # Only one element in the list
            self.head = None
            self.tail = None

        else:
            # Move tail pointer backwards
            self.tail = self.tail.previous

            # Disconnect old tail node
            self.tail.next = None

        return value

    def remove(self, node):
        """
        Remove a node from the list using its reference.

        Time Complexity: O(1)

        Args:
            node (Node): the node to remove
        """
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous = None
        node.next = None
