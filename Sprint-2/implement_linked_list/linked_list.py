class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, data):
        new_head_node = Node(data)
        if self.head is not None:
            new_head_node.next = self.head
            self.head.prev = new_head_node
        
        self.head = new_head_node
        if self.tail is None:
            self.tail = new_head_node

        return new_head_node
    


    def pop_tail(self):
        if self.tail is not None:
            tail_node = self.tail
            node = self.tail.prev
            self.tail = node
            self.tail.next = None
            self.tail.prev != None
          
