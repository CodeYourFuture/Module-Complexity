
#each node should know what comes before it and what come after it 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
        self.previous = None #to implement a 0(1) we need a implement a double linked list to access previous.

#for O(1), track both ends
class LinkedList:
    def __init__(self):
        self.head = None   
        self.tail = None

    def push_head(self,value): 
        new_node = Node(value)
        if self.head is None:  
            self.head = self.tail = new_node
            return new_node
        
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

        return new_node
    
#Remove last node 
    def pop_tail(self):
        if self.tail is None: 
            return None 
        removed = self.tail 
        self.remove(removed) 
        return removed.value
    
    def remove(self, node):
        if node.previous is not None: #fixing previous link
            node.previous.next = node.next
        else:

            self.head = node.next # removing the head

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous # removing the tail
#Detach the node
        node.next = None
        node.previous = None