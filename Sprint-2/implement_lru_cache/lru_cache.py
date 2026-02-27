from collections import OrderedDict

class LruCache:
    def __init__(self, limit):
        self.limit = limit
        self.cache = OrderedDict()

    def set(self, key, value):
        self.cache[key] = value
        
    def get(self, key):
        return self.cache[key]
