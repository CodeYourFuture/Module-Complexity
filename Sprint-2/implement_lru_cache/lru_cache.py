class LruCache:
    def __init__(self, limit):
        self.limit = limit
        self.cache = {}

    def set(self, key, value):
        self.key = key
        self.cache[key] = value
        