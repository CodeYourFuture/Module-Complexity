class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

# [1, 2 ] - 4
    def push_head(self, value): # add element to the start of list.
        handle = Node(value)
        handle.next = self.head

        if self.head:
            self.head.previous = handle
        else:
            self.tail = handle
        
        self.head = handle
        return handle

# [4, 1, 2]
    def pop_tail(self): # remove element from end of list
        if not self.tail:
            return None
        
        old_tail = self.tail
        value = self.tail.value
        new_tail = self.tail.previous

        if new_tail:
            new_tail.next = None
        else:
            self.head = None
        
        self.tail = new_tail

        old_tail.previous = None
        old_tail.next = None

        return value

# [4, 1, 2] - 1
    def remove(self, handle): # takes handle from 'push_head' + remove it
        if handle.previous: #4
            handle.previous.next = handle.next
        else:
            self.head = None

        if handle.next: #2
            handle.next.previous = handle.previous
        else:
            self.tail = handle.previous

        handle.next = None
        handle.previous = None