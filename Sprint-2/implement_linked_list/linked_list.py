class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def push_head(self, value): #this is to add a value/node to the head/start.
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.previous = node
        self.head = node
        if not self.tail:
            self.tail = node #list=empty,tail also points to new node
        return node
    def pop_tail(self): #Remove the value from the tail of the list
        if not self.tail:
            return None 
        value = self.tail.value
        prev_node = self.tail.previous
        if prev_node:
            prev_node.next = None
        self.tail = prev_node
        if not self.tail:
            self.head = None #If only one element is removed.
        return value
    def remove(self, node): #remove any node 
        if not node:
            return
        prev_node = node.previous
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.previous = prev_node
        else:
            self.tail = prev_node
        node.next = None     #Disconnecting the node from the rest
        node.previous = None
# My analysis
# the algorithm used on this linked list is efficient each methods have only O(1) space and time complexity since they operate on a single node at a time
# and at the start of the program we just created a class at a time with similar time and space complexity of O(n)