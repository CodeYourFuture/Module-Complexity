class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be greater than 0")
        self.limit = limit
        self.keys = {}
        self.linkedList = LinkedList()
    
    def get(self, key):
        if key not in self.keys:
            return None
        else:
            self.linkedList.remove(self.keys[key])
            self.linkedList.push_head(self.keys[key])
            return self.keys[key].data
    
    def set(self, key, data):
        if key not in self.keys:
            if len(self.keys) >= self.limit:
                node_to_delete = self.linkedList.pop_tail()
                del self.keys[node_to_delete.key]
            self.keys[key] = Node(key, data)
            self.linkedList.push_head(self.keys[key])

        else:
            self.keys[key].data = data
            self.linkedList.push_head(self.keys[key])

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_head(self, new_node):
        new_node.previous = None
        new_node.next = None
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        return new_node
    
    def remove(self, node):
        if node is None:
            return
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.previous
        if node.previous is not None:
            node.previous.next = node.next
        if node.next is not None:
            node.next.previous = node.previous
        node.next = None
        node.previous = None
    
    def pop_tail(self):
        if self.tail is None:
            return None
        node_to_pop = self.tail
        self.remove(self.tail)
        return node_to_pop