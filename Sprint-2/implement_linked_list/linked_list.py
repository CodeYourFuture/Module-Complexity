class Node: #A node in a doubly linked list
    def __init__(self, value): #Initialize a new node with the given value and no next or previous nodes
        self.value = value
        self.previous = None
        self.next = None


class LinkedList: # A doubly linked list data structure
    def __init__(self): # Initialize an empty linked list with no head node
        self.head = None
        self.tail = None

    def push_head(self, value): # Add a new node with the given value to the head of the list
        new_node = Node(value) # Create a new node with the given value

        new_node.next = self.head # Set the new node's next pointer to the current head of the list
        if self.head: # If the list is not empty, set the current head's previous pointer to the new node
            self.head.previous = new_node
        else:
            self.tail = new_node

        self.head = new_node # Update the head of the list to be the new node
        return new_node   # Return node for O(1) removal later

    def remove(self, node): # Remove the given node from the list
        if node.previous:
            node.previous.next = node.next
        else:
            # Removing head
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            # Removing tail
            self.tail = node.previous

        # Clean up references
        node.previous = None
        node.next = None

    def pop_tail(self):
        if not self.tail:
           return None

        old_tail = self.tail
        value = old_tail.value

        if old_tail.previous:
          self.tail = old_tail.previous
          self.tail.next = None
        else:
           # Only one element
           self.head = None
           self.tail = None

        return value

