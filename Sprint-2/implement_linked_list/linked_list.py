# A single node in the list
class ListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
# The linked list class
class LinkedList:
    def __init__(self):        
        self.head = None        
        self.tail = None

    # Add a value to the front of the list
    def push_head(self, value):        
        new_node = ListNode(value)        
        new_node.next = self.head

        if self.head:
            self.head.previous = new_node

        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        return new_node
    
    # Remove and return value from the end
    def pop_tail(self):
        if self.tail is None:
            return None

        value = self.tail.value

        if self.tail.previous:
            self.tail = self.tail.previous
            self.tail.next = None
        else:            
            self.head = None
            self.tail = None

        return value
    
    # Remove a node from the list
    def remove(self, node):
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