from linked_list import LinkedList, Node

class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than 0")
        
        self.limit = limit
        self.lookup = {}
        self.list = LinkedList()  

    def get(self, key):
        if key not in self.lookup:
            return None
            
        node = self.lookup[key]
        value = node.value
        
        self.list.remove(node)
        self.lookup[key] = self.list.push_head(key, value)
        return value

    def set(self, key, value) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            self.list.remove(node)
            self.lookup[key] = self.list.push_head(key, value)
        else:
            
            if len(self.lookup) >= self.limit:
                oldest_node = self.list.pop_tail()
                if oldest_node is not None:
                    del self.lookup[oldest_node.key]  
                       
            
            self.lookup[key] = self.list.push_head(key, value)