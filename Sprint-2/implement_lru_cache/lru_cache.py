from collections import OrderedDict

class LruCache:
    # It keeps the most recently used items.
    # If it gets full, it throws away the item we haven't used for the longest time.
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be positive")
        
        self.limit = limit
        # OrderedDict is like a dictionary. It remembers the order of items.
        # It handles the O(1) logic for us automatically.
        self.cache = OrderedDict()

    def get(self, key):
        # Trying to find an item
        if key not in self.cache:
            return None
        
        # If I found it, it means I just "USED" it.
        # So I move it to the end (Newest position).
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        # We are adding or updating an item.
        
        if key in self.cache:
            # If it exists, update it and move to the end (Newest).
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        if len(self.cache) > self.limit:
            # Remove the oldest item.
            # last=False means "Remove from the beginning (Oldest)".
            self.cache.popitem(last=False)