class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, data):
        new_head_node = Node(data)
        if self.head is not None:
            new_head_node.next = self.head
            self.head.previous = new_head_node

        self.head = new_head_node
        if self.tail is None:
            self.tail = new_head_node

        return new_head_node
    


    def pop_tail(self):
        if self.tail is None:
            raise IndexError("Unable to remove from empty linked list")

        tail_node = self.tail
        previous = self.tail.previous
        self.tail = previous
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        
        return tail_node.data
    


    def remove(self, node):
        previous_node = node.previous
        next_node = node.next

        if node.previous is not None:
            previous_node.next = next_node
        else:
            self.head = next_node

        if node.next is not None:
            next_node.previous = previous_node
        else:
            self.tail = previous_node

        node.previous = None
        node.next = None

  








            
          
          
