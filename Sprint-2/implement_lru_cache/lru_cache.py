#a node class is created with key,value... key is used to evict a specific char
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None