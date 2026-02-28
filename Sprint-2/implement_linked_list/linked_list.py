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
        if self.head is None:
            return None
        node_value = self.tail.value
        self.remove(self.tail)
        return node_value    
    
    def remove(self,node) -> None:
        node_to_remove=node
        current_head=self.head
        current_tail=self.tail
        if current_head==current_tail:
            #linkedlist has only one node
            self.head=None
            self.tail=None
        elif node_to_remove.next is None:
            #Node is the last node(tail)
            self.tail=node_to_remove.previous  
            self.tail.next=None  
        elif node_to_remove.previous is None:
            #Node is the first node(head)   
            self.head=node_to_remove.next
            self.head.previous=None
        else:
            #Node is in the middle of list
            previous_node=node_to_remove.previous        
            next_node=node_to_remove.next
            previous_node.next=next_node
            next_node.previous=previous_node

        node_to_remove.next=None
        node_to_remove.previous=None         
        
    

