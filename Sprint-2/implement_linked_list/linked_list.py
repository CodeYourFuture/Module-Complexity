# //operations
# `push_head` should add an element to the start of the list. 
# It should return something that can be passed to `remove` to 
# remove that element in the future.

    

# `pop_tail` should remove an element from the end of the list.
# * `remove` takes a handle from `push_head`, 
# and removes that element from the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def push_head(self, item_to_insert):
        # //wrap item to insert in {}
        wrapped_item = Node(item_to_insert)

        if not self.head:
            self.head = self.tail = wrapped_item
        else:
            wrapped_item.next = self.head
            self.head.previous = wrapped_item
            self.head = wrapped_item

        return wrapped_item

    def remove(self, id_for_this_particular_item):
        node_to_remove = id_for_this_particular_item
        
        if node_to_remove.previous:
            node_to_remove.previous.next = node_to_remove.next
        else:
            self.head = node_to_remove.next

        if node_to_remove.next:
            node_to_remove.next.previous = node_to_remove.previous
        else:
            self.tail = node_to_remove.previous

        #save data here
        saved_data = node_to_remove.data
        node_to_remove.next = node_to_remove.previous = None
        return saved_data

    def pop_tail(self):
        if not self.tail:
            return None
        return self.remove(self.tail)
