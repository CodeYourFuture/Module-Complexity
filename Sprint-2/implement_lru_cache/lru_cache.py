from collections import OrderedDict
from typing import Any, Optional
class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Limit must be a positive number")
        
        self._limit = limit
        self.cache = OrderedDict()
    
    def get(self, key: Any) -> Optional[Any]: # lookup the v previously associated with k
        if key not in self.cache:
            return None
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: Any, value: Any) -> None: # should associate k with passed v 
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            if len(self.cache) > self._limit:
                self.cache.popitem(last=False)