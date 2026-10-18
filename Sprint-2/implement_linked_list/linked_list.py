#node class to hold value and pointer
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None   # pointer to next node
        self.prev = None   # pointer to previous node

#LinkedList class to manage chain of nodes

class LinkedList:
    def __init__(self):
        self.head = None  # pointer to head
        self.tail = None  # pointer to tail

#insert at the beginning 

    def push_head(self,data):
        new_node = Node(data)

        if not self.head:     #if the node is empty it will have both head & tail
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head    # pointer to next new node 
            self.head.prev = new_node   # pointer back to old node by new node
            self.head = new_node        # move head pointer to new_node
        
        return new_node
    
   #remove data from last node & show the value
    def pop_tail(self):
        if not self.tail:      #if list is empty nothing to pop
            return None 
        tail_node = self.tail
        removed_data = tail_node.data  # save value to return later

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return removed_data
    
    #remove specific node

    def remove(self,node):
        
        #do  list is empty 
        if not self.head:
            return

        # if node is head move head to next node 
        if node == self.head:
            self.head = node.next

        #if node is tail move tail to prev node 
        if node == self.tail:
            self.tail = node.prev

        #unlink node from its neighbors 
        # check is there a node before 
        if node.prev:
            node.prev.next = node.next
        #check is there a node after
        if node.next:
            node.next.prev = node.prev

        # clean up pointers on the removed node

        node.prev = None
        node.next = None


        
        

        