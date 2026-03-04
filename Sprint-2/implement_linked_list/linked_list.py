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

    def push_head(self, item_to_insert):
        # //wrap item to insert in {}
        wrapped_item = Node(None, item_to_insert)

        if not self.head:
            self.head = self.tail = wrapped_item
        else:
            wrapped_item.next = self.head
            self.head.prev = wrapped_item
            self.head = wrapped_item

        # self.our_list.insert(0, wrapped_item)
        self.tracker_number +=1
        return wrapped_item

    def remove(self, id_for_this_particular_item):
        node_to_remove = id_for_this_particular_item
        
        if node_to_remove.prev:
            node_to_remove.prev.next = node_to_remove.next
        else:
            self.head = node_to_remove.next

        if node_to_remove.next:
            node_to_remove.next.prev = node_to_remove.prev
        else:
            self.tail = node_to_remove.prev

        return node_to_remove.inserted_item_key

    def pop_tail(self):
        if not self.tail:
            return None
        return self.remove(self.tail)
