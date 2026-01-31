import random


class _Node:
    def __init__(self, value, level):
        self.value = value
        # forward[i] is the next node at level i
        self.forward = [None] * (level + 1)


class SkipList:
    MAX_LEVEL = 16
    P = 0.5  # probability for level increase

    def __init__(self):
        # head is a dummy node with no value but MAX_LEVEL pointers
        self.head = _Node(None, self.MAX_LEVEL)
        self.level = 0  # current highest level in use
        self.size = 0

    def _random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, value):
        """Insert value in sorted order."""
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        # 1) Search for position from top level down
        for lvl in range(self.level, -1, -1):
            while current.forward[lvl] is not None and current.forward[lvl].value < value:
                current = current.forward[lvl]
            update[lvl] = current

        # 2) Check if already present -> do nothing
        next_node = current.forward[0]
        if next_node is not None and next_node.value == value:
            return

        # 3) Choose random level for new node
        new_level = self._random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level

        # 4) Insert node, fixing pointers at each level
        new_node = _Node(value, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

        self.size += 1

    def __contains__(self, value):
        """Implements `value in sl` using fast skip-list search."""
        current = self.head
        for lvl in range(self.level, -1, -1):
            while current.forward[lvl] is not None and current.forward[lvl].value < value:
                current = current.forward[lvl]
        current = current.forward[0]
        return current is not None and current.value == value

    def to_list(self):
        """Return all values in sorted order from the bottom level."""
        result = []
        current = self.head.forward[0]
        while current is not None:
            result.append(current.value)
            current = current.forward[0]
        return result
