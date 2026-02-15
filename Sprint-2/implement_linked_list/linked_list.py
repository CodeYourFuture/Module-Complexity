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
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
           old_head=self.head
           self.head=new_node
           new_node.next=old_head
           old_head.previous=new_node
        return new_node
    
    def pop_tail(self) -> any:
        pass
    def remove(self,node) -> None:
        pass

