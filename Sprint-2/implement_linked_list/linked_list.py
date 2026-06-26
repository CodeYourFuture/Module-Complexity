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
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        return new_node
    
    def remove(self, node):
        if node is None:
            return
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.previous
        if node.previous is not None:
            node.previous.next = node.next
        if node.next is not None:
            node.next.previous = node.previous
        node.next = None
        node.previous = None
    
    def pop_tail(self):
        if self.tail is None:
            return None
        node_to_pop = self.tail
        data = node_to_pop.data
        self.remove(node_to_pop)
        return data


    
