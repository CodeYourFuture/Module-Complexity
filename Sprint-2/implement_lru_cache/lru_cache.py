from collections import OrderedDict

class LruCache:
    # TASK
    # `LruCache(limit)` should construct 
    # an LRU cache which never stores more than `limit` entries.
    def __init__(self, user_limit):
        self.limit = user_limit
        self.our_key_dictionary = OrderedDict()

    # TASK
    # `set(key, value)` should associate `value` with the passed `key`.
    def set(self, key, value):
        
        if key in self.lookup_map:
            old_item = self.lookup_map[key]
            self.our_key_dictionary.pop(key)                
        wrapped_item = {
            "key": key,
            "value": value,
        }
        
        self.our_key_dictionary[key] = wrapped_item
        self.our_key_dictionary.move_to_end(key, last=False)
        
        if len(self.our_key_dictionary) > self.limit:
            self.our_key_dictionary.popitem()

    def get(self, key):
        if key in self.our_key_dictionary:
            item = self.our_key_dictionary[key]
            self.our_key_dictionary.move_to_end(key, last=False)

            return item["value"]
        return None

