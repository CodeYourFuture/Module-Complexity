from collections import OrderedDict

class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be positive")

        self.limit = limit
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None

        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache) >= self.limit:
            self.cache.popitem(last=False)

        self.cache[key] = value