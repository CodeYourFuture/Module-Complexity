import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)  # forward pointers for each level

class SkipList:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.header = Node(None, self.MAX_LEVEL)
        self.level = 0 

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        # Move down from top level to bottom to find insert positions
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        # Insert only if not already present
        if current is None or current.value != value:
            lvl = self.random_level()
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = Node(value, lvl)
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def contains(self, value):
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == value

    def to_list(self):
        result = []
        current = self.header.forward[0]
        while current:
            result.append(current.value)
            current = current.forward[0]
        return result
