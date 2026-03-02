# //operations
# `push_head` should add an element to the start of the list. 
# It should return something that can be passed to `remove` to 
# remove that element in the future.

    

# `pop_tail` should remove an element from the end of the list.
# * `remove` takes a handle from `push_head`, 
# and removes that element from the list.
class Node:
    def __init__(self, tracker, inserted_item_key):
        self.tracker = tracker
        self.inserted_item_key = inserted_item_key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
        self.tracker_number = 0
        self.our_list = []
        

    def push_head(self, item_to_insert):
        # assign so gets updated
        id_for_this_particular_item = self.tracker_number
        # //wrap item to unsert in {}
        wrapped_item = Node(id_for_this_particular_item, item_to_insert)

        if self.head is None:
            self.head = self.tail = wrapped_item
        else:
            wrapped_item.next = self.head
            self.head.prev = wrapped_item
            self.head = wrapped_item

        self.our_list.insert(0, wrapped_item)
        self.tracker_number +=1
        return id_for_this_particular_item

    def remove(self, id_for_this_particular_item):
        for node in self.our_list:
            if node.tracker == id_for_this_particular_item:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next

                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev

                self.our_list.remove(node)
                return node.inserted_item_key
            
    def pop_tail(self):
        if not self.our_list:
            return None

        old_tail = self.tail
        if old_tail.prev:
            self.tail = old_tail.prev
            self.tail.next = None
        else:
            self.head = self.tail = None

        if len(self.our_list) > 0:
            self.our_list.pop()
            return old_tail.inserted_item_key
                
