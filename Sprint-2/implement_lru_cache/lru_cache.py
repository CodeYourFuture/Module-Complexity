from collections import OrderedDict

class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self.limit = limit
        # Store items in order used
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None  
        # Mark as recently used      
        self.cache.move_to_end(key)
        # Return the value
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache: 
            # Mark as recently used     
            self.cache.move_to_end(key)
        self.cache[key] = value
        # Set or update value
        if len(self.cache) > self.limit:   
            # Remove least used        
            self.cache.popitem(last=False)
