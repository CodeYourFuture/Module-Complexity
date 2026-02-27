class LruCache:
    def __init__(self, limit):
        self.limit = limit
        self.cache = {}