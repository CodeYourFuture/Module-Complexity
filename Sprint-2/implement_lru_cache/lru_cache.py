from collections import OrderedDict

class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self.limit = limit
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None

        # Mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            
            self.cache.move_to_end(key)

        self.cache[key] = value

        # Evict least recently used item
        if len(self.cache) > self.limit:
            self.cache.popitem(last=False)
