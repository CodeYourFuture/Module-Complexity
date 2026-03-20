import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * (level + 1) # next[i] the next node at level i


class SkipList:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = Node(None, self.MAX_LEVEL)
        self.level = 0          # highest level currently in use

    def _random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        # Find the place where the new value should go
        for level in range(self.level, -1, -1):
            while current.next[level] and current.next[level].value < value:
                current = current.next[level]
            update[level] = current

        next_node = current.next[0]
        if next_node and next_node.value == value:
            return

        node_level = self._random_level()

        if node_level > self.level:
            for level in range(self.level + 1, node_level + 1):
                update[level] = self.head
            self.level = node_level

        new_node = Node(value, node_level)
        for level in range(node_level + 1):
            new_node.next[level] = update[level].next[level]
            update[level].next[level] = new_node
    
    # Check if value exists
    def contains(self, value):
        current = self.head
        for level in range(self.level, -1, -1):
            while current.next[level] and current.next[level].value < value:
                current = current.next[level]

        candidate = current.next[0]
        return candidate is not None and candidate.value == value

    def __contains__(self, value):
        return self.contains(value)

    def to_list(self):
        result = []
        current = self.head.next[0]
        while current:
            result.append(current.value)
            current = current.next[0]
        return result

    
