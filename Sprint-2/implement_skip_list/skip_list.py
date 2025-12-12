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
        x = self.head

        # Find the place where the new value should go
        for i in range(self.level, -1, -1):
            while x.next[i] and x.next[i].value < value:
                x = x.next[i]
            update[i] = x

        x0 = x.next[0]
        if x0 and x0.value == value:
            return

        node_level = self._random_level()

        if node_level > self.level:
            for i in range(self.level + 1, node_level + 1):
                update[i] = self.head
            self.level = node_level

        new_node = Node(value, node_level)
        for i in range(node_level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
    
    # Check if value exists
    def contains(self, value):
        x = self.head
        for lvl in range(self.level, -1, -1):
            while x.next[lvl] and x.next[lvl].value < value:
                x = x.next[lvl]

        x = x.next[0]
        return x is not None and x.value == value

    def __contains__(self, value):
        return self.contains(value)

    def to_list(self):
        result = []
        x = self.head.next[0]
        while x:
            result.append(x.value)
            x = x.next[0]
        return result

    
