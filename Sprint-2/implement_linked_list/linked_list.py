class Node:
    __slots__ = ("value", "next", "previous")

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    __slots__ = ("head", "tail")

    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        
        return new_node
    
    def pop_tail(self):

        if self.tail == None:
            return None

        return self.remove(self.tail)

    def remove(self, node):
        if self.head == None and self.tail == None:
            return None
        
        new_previous = node.previous
        new_next = node.next

        val = node.value

        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif self.head == node :
            new_next.previous = None
            self.head = new_next
        elif self.tail == node:
            new_previous.next = None
            self.tail = new_previous
        elif new_next and new_previous:
            new_previous.next = new_next
            new_next.previous = new_previous

        node.previous = None
        node.next = None
        return val

    def push_tail(self, value):
        new_node = Node(value)

        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        return new_node
        