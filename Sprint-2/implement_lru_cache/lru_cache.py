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
    

#Lru class for the logic
class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than zero")
        self.limit = limit
        self.cache = {}  #key->Node
        self.dll = DoublyLinkedList()
    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return None
        # Move the node to the head (most recently used)
        self.dll._move_to_head(node)
        return node.value
    def set(self, key, value):
        node = self.cache.get(key)
        if node:
            # Update existing node and move it to head
            node.value = value
            self.dll._move_to_head(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.dll._add_to_head(new_node)
            if len(self.cache) > self.limit:
                # Remove least recently used node
                tail = self.dll._pop_tail()
                del self.cache[tail.key]
