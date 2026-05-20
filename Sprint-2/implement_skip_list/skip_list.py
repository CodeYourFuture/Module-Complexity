import random


class Node:
    def __init__(self, height, value):
        self.value = value
        self.forward = [None] * height


class SkipList:
    MAX_HEIGHT = 16
    P = 0.5

    def __init__(self):
        self.head = Node(self.MAX_HEIGHT, None)
        self.level = 1
        self.length = 0

    def __len__(self):
        return self.length

    def random_height(self):
        height = 1
        while random.random() < self.P and height < self.MAX_HEIGHT:
            height += 1
        return height

    def _find_updated_path(self, value):
        update = [None] * self.MAX_HEIGHT
        current = self.head
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        return update

    def __contains__(self, value):
        current = self.head

        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]

        current = current.forward[0]
        return current is not None and current.value == value

    def insert(self, value):
        update = self._find_updated_path(value)
        forward_node = update[0].forward[0]

        if forward_node and forward_node.value == value:
            return
        node_height = self.random_height()
        if node_height > self.level:
            for i in range(self.level, node_height):
                update[i] = self.head
            self.level = node_height

        new_node = Node(node_height, value)

        for i in range(node_height):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
        self.length += 1

    def to_list(self):
        result = []
        current = self.head.forward[0]
        while current:
            result.append(current.value)
            current = current.forward[0]
        return result
