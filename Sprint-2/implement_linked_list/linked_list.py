class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None  
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value) -> Node:
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            
        return new_node

    def remove(self, node: Node) -> None:
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
        
        last_node = self.tail
        value = last_node.value
        
        self.remove(last_node)
        
        return value
    
