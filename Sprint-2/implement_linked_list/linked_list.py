# `push_head` should add an element to the start of the list. It should return something that can be passed to 
# `remove` to remove that element in the future.
# `pop_tail` should remove an element from the end of the list.
# `remove` takes a handle from `push_head`, and removes that element from the list.

class LinkedList:
    class _Node:  # to have O(1) must be implemented double linked list to access previous
        __slots__ = ("value", "prev", "next")

        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = self._Node(value)

        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            # when list gets empty, tail also becomes this node
            self.tail = node

        self.head = node
        return node  # handling

    def pop_tail(self):
        if not self.tail:
            raise IndexError("pop from empty list")

        node = self.tail
        value = node.value

        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            # when the list gets empty
            self.head = None

        return value

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            # removes head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            # removes tail
            self.tail = node.prev
