from collections import OrderedDict

class LruCache:
    def __init__(self, limit):
        self.limit = limit
        self.cache = OrderedDict()


    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.limit:
                self.cache.popitem(key)

        self.cache[key] = value
        


    def get(self, key):
        return self.cache[key]
