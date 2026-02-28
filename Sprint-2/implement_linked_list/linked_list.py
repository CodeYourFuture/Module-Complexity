# `push_head` should add an element to the start of the list. It should return something that can be passed to 
# `remove` to remove that element in the future.
# `pop_tail` should remove an element from the end of the list.
# `remove` takes a handle from `push_head`, and removes that element from the list.

class Node:
    def __init__(self, value):
        self.value = value      
        self.prev = None        
        self.next = None       


class LinkedList:
    def __init__(self):
        self.head = None        
        self.tail = None        

    # adding a new value in the front of the list
    def push_head(self, value):
        node = Node(value)      

        if self.head is None:   # if list is empty head and tail becomes this node.
            self.head = node    
            self.tail = node    
        else:
            node.next = self.head   
            self.head.prev = node   
            self.head = node        

        return node  # returns the node so we can remove it later

    # removing last element
    def pop_tail(self):
        if self.tail is None:   
            raise Exception("List is empty")

        value = self.tail.value  # value to return

        if self.head == self.tail:  # if only one element
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev  # move tail back
            self.tail.next = None       # remove old tail connection

        return value

    # removes a specific node 
    def remove(self, node):

        if node.prev is None:   # if removing head
            self.head = node.next
        else:
            node.prev.next = node.next  # connect previous to next

        if node.next is None:   # if removing tail
            self.tail = node.prev
        else:
            node.next.prev = node.prev  # connect next to previous