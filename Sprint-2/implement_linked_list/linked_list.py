class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
        if self.tail is None:
            self.tail = new_node

        return new_node
    
    def pop_tail(self):
        if self.tail is None:
            return
        node_to_be_removed = self.tail
        self.tail = node_to_be_removed.prev

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        
        return node_to_be_removed.value

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = node.prev
        node.prev = None
        node.next = None




