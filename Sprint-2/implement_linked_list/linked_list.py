class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, data):
        node = Node(data)

        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.previous = node
        self.head = node
        return node

    def remove(self, node):
        if node is None:
            return
        
        if node.previous is None:
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:
            self.tail = node.previous
        else:
            node.next.previous = node.previous
        node.previous = None
        node.next = None       
    
    def pop_tail(self):
        if self.head is None:
            return
        if self.tail is None:
            return None
        
        node = self.tail
        if node.previous is None:
            self.head = None
            self.tail = None
        else:
            self.tail = node.previous
            self.tail.next = None
        node.previous = None
        node.next = None
        return node.data


