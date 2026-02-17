class Node:
    # This class is for the Node (the item).
    # It keeps the value and pointers to next and previous.
    def __init__(self, value):
        self.value = value
        self.next = None       # Pointer to next node
        self.previous = None   # Pointer to previous node


class LinkedList:
    # This class controls the list.
    # It tracks head and tail. operations are O(1).
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        # Create a new node with the value
        new_node = Node(value)

        # If list is empty, head and tail is this new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # If list not empty, put new node at start
            new_node.next = self.head     # Link new node to old head
            self.head.previous = new_node # Link old head back to new node
            self.head = new_node          # Update head pointer

        return new_node

    def pop_tail(self):
        # Remove the last item (tail)
        if self.tail is None:
            return None

        value_to_return = self.tail.value

        # Check if only 1 item in list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # More than 1 item. Move tail pointer back.
            self.tail = self.tail.previous
            self.tail.next = None # Cut the link to the old tail

        return value_to_return

    def remove(self, node):
        # Remove a specific node from the list.
        # We just assume node is definitely in the list.
        
        # If removing the Head node
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None # List became empty
        
        # If removing the Tail node
        elif node == self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

        # If removing a node in the middle
        else:
            # Link previous node to the next node
            node.previous.next = node.next
            # Link next node to the previous node
            node.next.previous = node.previous