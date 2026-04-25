class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # Pointer to the next node in the list.
        self.previous = None # a pointer to the previous node so the removal can be done in constant time

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        return new_node

    def pop_tail(self):
        if not self.tail:
            return None
        
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            
        return removed_value

    def remove(self, node):
        if not node:
            return
       
        if node == self.head:
            self.head = node.next

       
        if node == self.tail:
            self.tail = node.previous

    
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous

     
        node.next = node.previous = None