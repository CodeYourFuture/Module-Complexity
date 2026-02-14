class Node:
    __slots__ = ("value", "previous", "next")

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = Node(value)

        if self.head is None:
            # empty list
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        return node  #This is the handle
    
    def pop_tail(self):
        if self.tail is None:
            raise IndexError("Pop from empty list")
        
        node = self.tail

        if node.previous is None:
            # One element
            self.head = self.tail = None
        else:
            self.tail = node.previous
            self.tail.next = None
        
        return node.value
    
    def remove(self, node):
        if node.previous:
            node.previous.next = node.next

        else:
            # removing head
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            # removing the tail
            self.tail = node.previous

        # Clean up references

        node.previous = None
        node.next = None