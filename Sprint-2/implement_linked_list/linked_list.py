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
            return
        elif self.tail == self.head:
            val = self.tail.value
            self.tail = None
            self.head = None
            return val
        else:
            val = self.tail.value
            new_tail = self.tail.previous
            new_tail.next = None
            self.tail.previous = None
            self.tail = new_tail
            return val

    def remove(self, Node):
        if self.head == None and self.tail == None:
            return
        
        new_previous = Node.previous
        new_next = Node.next

        if self.head == Node and self.tail == Node:
            Node.value = None
            self.head = None
            self.tail = None
        elif self.head == Node :
            Node.previous = None
            Node.next = None
            new_next.previous = None
            self.head = new_next
        elif self.tail == Node:
            self.pop_tail()
        elif new_next and new_previous:
            new_previous.next = new_next
            new_next.previous = new_previous
            Node.previous = None
            Node.next = None

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
        