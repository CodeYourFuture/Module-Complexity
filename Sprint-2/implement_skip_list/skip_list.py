import random

class SkipNode:
    def __init__(self, value, height):
        self.value = value
        self.next = [None] * height

class SkipList:
    def __init__(self, max_height=16):
        self.max_height = max_height

        self.head = SkipNode(None, self.max_height)
        self.level = 1 

    def _random_height(self) -> int:
        height = 1
        while random.random() < 0.5 and height < self.max_height:
            height += 1
        return height

    def insert(self, value) -> None:
        update = [None] * self.max_height
        current = self.head

        for i in range(self.max_height - 1, -1, -1):
            while current.next[i] is not None and current.next[i].value < value:
                current = current.next[i]
            update[i] = current

        node_height = self._random_height()
        new_node = SkipNode(value, node_height)

        for i in range(node_height):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def __contains__(self, value) -> bool:
        current = self.head

        for i in range(self.max_height - 1, -1, -1):
            while current.next[i] is not None and current.next[i].value < value:
                current = current.next[i]

        current = current.next[0]
        return current is not None and current.value == value

    def to_list(self) -> list:
        result = []
        current = self.head.next[0]
        while current is not None:
            result.append(current.value)
            current = current.next[0]
        return result