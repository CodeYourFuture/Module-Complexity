
#linked list has nodes - each node has a value and a pointer to next node- who comes next. 
class node:
    def __init__(self,value):
        self.value = value
        self.next = None  #None means empty we are not yet pointing to another node yet
        pass
class linkedlist:
    def __init__(self):
        self.head = None   #head is the first element of a linked list 

    def append(self,value): 
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            return
    #creating a temperory pointer current to move forward safely 
        current = self.head #makes a copy of first head node with current being our temp pointer
        while current.next is not None: #head > next >  next > next >
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
ll = linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()