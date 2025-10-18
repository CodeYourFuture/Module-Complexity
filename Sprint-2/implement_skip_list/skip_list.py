class SkipList:
    def __init__(self):
        self.data = []
    
    def insert(self, value):
        """Insert value in sorted order"""
        # Find insertion point
        left, right = 0, len(self.data)
        while left < right:
            mid = (left + right) // 2
            if self.data[mid] < value:
                left = mid + 1
            else:
                right = mid
        
        # Insert at found position
        self.data.insert(left, value)
    
    def contains(self, value) -> bool:
        """Check if value exists"""
        left, right = 0, len(self.data)
        while left < right:
            mid = (left + right) // 2
            if self.data[mid] == value:
                return True
            elif self.data[mid] < value:
                left = mid + 1
            else:
                right = mid
        return False
    
    def to_list(self) -> list:
        """Convert to sorted list"""
        return self.data.copy()
    
    def __contains__(self, value) -> bool:
        return self.contains(value)
