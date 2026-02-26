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
        if self.tail is not None:
            tail_node = self.tail
            previous = self.tail.previous
            self.tail = previous
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
        else:
            raise IndexError("Unable to remove from empty linked list")
        
        return tail_node.data
    


    def remove(self, node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

  








            
          
          
