class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        
        self.limit = limit
        self.cache = {}
        self.access_order = []  # most recent at the end
        
    def get(self, key):
        if key in self.cache:
            # Move to most recent position
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None

    def set(self, key, value):
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            # Move to most recent position  
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # New key
            if len(self.cache) >= self.limit:
                # Remove least recently used (first item)
                lru_key = self.access_order[0]
                del self.cache[lru_key]
                self.access_order.pop(0)
            
            # Add new key as most recent
            self.cache[key] = value
            self.access_order.append(key)