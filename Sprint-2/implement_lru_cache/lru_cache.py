#a node class is created with key,value... key is used to evict a specific char
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

#next step i define helper functions to add and remove node : 
#I use the same concept of the previous project of the linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail #this is most recently used
        self.tail.previous = self.head  #this is the least recently used

    def _add_to_head(self, node):
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.previous
        nxt = node.next
        prev.next = nxt
        nxt.previous = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self):
        node = self.tail.previous
        self._remove_node(node)
        return node