import time

class LruCache:
    #  `LruCache(limit)` should construct 
    # an LRU cache which never stores more than `limit` entries.
    def __init__(self, user_limit):
        self.limit = user_limit
        self.our_list = []  
        self.lookup_map = {} 

    # * `set(key, value)` should associate `value` with the passed `key`.
    def set(self, key, value):
        
        if key in self.lookup_map:
            old_item = self.lookup_map[key]
            self.our_list.remove(old_item)
                
        wrapped_item = {
            "key": key,
            "value": value,
        }
        
    #add to list and map
        self.our_list.insert(0, wrapped_item)
        self.lookup_map[key] = wrapped_item
        
    #if full remove oldest timestamp so last
        if len(self.our_list) > self.limit:
            oldest_item = self.our_list.pop() 
            
            del self.lookup_map[oldest_item["key"]]


    # * `get(key)` should look-up the value previously associated with `key`.
    def get(self, key):
    #check map instead of for loop    
        if key in self.lookup_map:
            # find by key
            item = self.lookup_map[key]
            
            #move to front
            self.our_list.remove(item)
            self.our_list.insert(0, item)
            
            return item["value"]
        return None

