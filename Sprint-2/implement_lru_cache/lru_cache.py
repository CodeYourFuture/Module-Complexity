class Node:
    """Represents a single node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Manages a doubly linked list with sentinel head and tail nodes."""
    
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        """Add a node to the front of the list (right after head)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        """Remove a node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get_least_recent(self):
        """Get the least recently used node (just before tail)."""
        return self.tail.prev


class LruCache:
    """LRU Cache implementation using a doubly linked list to track usage order."""
    
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = limit
        self.cache = {}
        self.linked_list = DoublyLinkedList()

    def get(self, key):
        """Get a value from the cache and mark it as recently used."""
        if key not in self.cache:
            return None

        node = self.cache[key]
        self.linked_list.remove(node)
        self.linked_list.add_to_front(node)
        return node.value

    def set(self, key, value):
        """Set a value in the cache, evicting the LRU item if at capacity."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.linked_list.remove(node)
            self.linked_list.add_to_front(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.linked_list.add_to_front(new_node)

            if len(self.cache) > self.capacity:
                lru = self.linked_list.get_least_recent()
                self.linked_list.remove(lru)
                del self.cache[lru.key]
