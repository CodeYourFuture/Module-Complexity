from collections import OrderedDict


class LruCache:
    def __init__(self, limit):
        if limit < 1:
            raise ValueError("Limit cannot be less than 1")
        self.limit = limit
        self.storage = OrderedDict()

    def set(self, key, value):
        if len(self.storage) == self.limit:
            if key in self.storage:
                self.storage.move_to_end(key)
            else:
                self.storage.popitem(last=False)
        self.storage[key] = value

    def get(self, key):
        if key in self.storage:
            self.storage.move_to_end(key)
            return self.storage[key]
        return None
