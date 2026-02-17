class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_head(self, value):
        """Add an element to the start of the list. Returns a handle to the node."""
        new_node = self.Node(value)
        
        if self.head is None:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # Add to front
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        
        return new_node
    
    def pop_tail(self):
        """Remove and return the element from the end of the list."""
        if self.tail is None:
            raise IndexError("pop from empty list")
        
        value = self.tail.value
        
        if self.head == self.tail:
            # Only one element
            self.head = None
            self.tail = None
        else:
            # Multiple elements
            self.tail = self.tail.previous
            self.tail.next = None
        
        return value
    
    def remove(self, node):
        """Remove a specific node from the list using the handle from push_head."""
        if node is None:
            return
        
        if node.previous is not None:
            node.previous.next = node.next
        else:
            # node is head
            self.head = node.next
        
        if node.next is not None:
            node.next.previous = node.previous
        else:
            # node is tail
            self.tail = node.previous
        
        # Clean up references
        node.next = None
        node.previous = None