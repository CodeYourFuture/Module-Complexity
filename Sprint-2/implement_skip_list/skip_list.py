import random


class SkipListNode:
    """Node in a skip list with multiple forward pointers"""
    def __init__(self, value, levels):
        self.value = value
        self.forward = [None] * levels


class SkipList:
    def __init__(self):
        self.max_level = 16
        self.head = SkipListNode(float('-inf'), self.max_level)
        self.level = 0
    
    def _random_level(self):
        """Generate random level for a new node (coin flip)"""
        level = 0
        while random.random() < 0.5 and level < self.max_level - 1:
            level += 1
        return level
    
    def insert(self, value):
        """Insert value in sorted order - O(log n) time complexity"""
        update = [None] * self.max_level
        current = self.head
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        new_level = self._random_level()
        
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level
        
        new_node = SkipListNode(value, new_level + 1)
        
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
    
    def contains(self, value) -> bool:
        """Check if value exists - O(log n) time complexity"""
        current = self.head
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        
        current = current.forward[0]
        return current is not None and current.value == value
    
    def to_list(self) -> list:
        """Convert to sorted list - O(n) time complexity"""
        result = []
        current = self.head.forward[0]
        while current:
            result.append(current.value)
            current = current.forward[0]
        return result
    
    def __contains__(self, value) -> bool:
        return self.contains(value)
