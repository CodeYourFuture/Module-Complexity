import random

class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * (level + 1)  # Next nodes at each level

class SkipList:
    def __init__(self):
        self.max_level = 16
        self.head = SkipListNode(None, self.max_level)  # Head node
        self.level = 0  # Current highest level
        self.size = 0
    
    def _random_level(self):
        """Generate random level for a new node (coin flip)"""
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level
    
    def __contains__(self, key):
        """Support 'in' operator"""
        return self.contains(key)
    
    def contains(self, key):
        """Check if key exists in the skip list"""
        current = self.head
        
        # Start from highest level and move down
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < key:
                current = current.next[i]
        
        # Move to the node that might contain the value
        current = current.next[0]
        return current is not None and current.value == key
    
    def insert(self, value):
        """Insert a value into the skip list"""
        update = [None] * (self.max_level + 1)
        current = self.head
        
        # Find the position to insert and track update pointers
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
            update[i] = current
        
        current = current.next[0]
        
        # If value already exists, we'll still insert it (allow duplicates)
        new_level = self._random_level()
        
        # Update the max level if needed
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level
        
        # Create new node
        new_node = SkipListNode(value, new_level)
        
        # Update pointers at each level
        for i in range(new_level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
        
        self.size += 1
    
    def to_list(self):
        """Convert skip list to a sorted list"""
        result = []
        current = self.head.next[0]  # Start from first element at level 0
        
        while current:
            result.append(current.value)
            current = current.next[0]
        
        return result
    
    def __str__(self):
        """String representation for debugging"""
        result = []
        for level in range(self.level, -1, -1):
            level_str = f"Level {level}: "
            current = self.head.next[level]
            elements = []
            while current:
                elements.append(str(current.value))
                current = current.next[level]
            level_str += " -> ".join(elements) if elements else "empty"
            result.append(level_str)
        return "\n".join(result)