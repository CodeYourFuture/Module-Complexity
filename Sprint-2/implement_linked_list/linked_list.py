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
        """Add a value to the head. Return the node as a handle."""
        node = Node(value)
        node.next = self.head

        if self.head:
            self.head.previous = node
        self.head = node
        if not self.tail:
            self.tail = node      #list=empty,tail also points to new node
        return node

    def pop_tail(self):
        if not self.tail:
            return None 
        value = self.tail.value
        prev_node = self.tail.previous
        if prev_node:
            prev_node.next = None
        self.tail = prev_node

        
        if not self.tail:
            self.head = None #If we removed the only element

        return value

    def remove(self, node):
        if not node:
            return
        prev_node = node.previous
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.previous = prev_node
        else:
            self.tail = prev_node
        node.next = None     # Disconnect node
        node.previous = None
