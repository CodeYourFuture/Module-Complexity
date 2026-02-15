class Node:
    """
    Represents a node in a doubly linked list.
    Each node holds a value and references to the previous and next nodes.
    """
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous=None

class LinkedList:
    """
    A doubly linked list supporting push_head, pop_tail, and remove operations.
    Maintains references to both head and tail nodes for O(1) operations.
    """
    def __init__(self):
        self.head=None
        self.tail=None        
    def push_head(self,value) -> Node:
        pass
    def pop_tail(self) -> any:
        pass
    def remove(self,node) -> None:
        pass
