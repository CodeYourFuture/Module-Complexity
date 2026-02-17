
#each node should know what comes before it and what come after it 
class node:
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
        new_node = node(value)
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
        #checking for 1 elemt
        if self.head == self.tail: 
           self.head = self.tail = None 
           return removed.value
        
        #Greater than 1 element, move tailpointer to previos
        self.tail = self.tail.previous 
        self.tail.next = None #cutting link to old tail
        return removed.value
    
    def remove(self, node):
        if node.previous is not None: #fixing previous link
            node.previous.next = node.next
        else:
            # removing the head
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
        # removing the tail
        
            self.tail = node.previous
