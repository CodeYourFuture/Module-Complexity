from linked_list import LinkedList, Node

class LruCache:
    def __init__(self,limit):
        """
        Initialize the LRU Cache.
        Args: limit (int): Maximum number of items the cache can hold.
        """
        if limit<=0:
            raise ValueError("limit must be greater than zero")
        self.limit=limit
        self.map={}
        self.List=LinkedList()
        self.count=0

    def get(self,key) ->any:
        """
        Retrieve value by key and mark node as most recently used.
        Args: key: Key to look up in cache.
        Returns: The value associated with the key, or None if not found.
        """
        if key not in self.map:
            return None
        node=self.map[key]   
        self.List.push_head(node=node)
        return node.value  


    def set(self,key,value):
        """
        Add a new key-value pair or update an existing key.
        Args:
            key: Key to insert or update.
            value: Value to associate with the key.
        Behavior:
            - Updates value if key exists and moves node to head.
            - Inserts new node at head if key does not exist.
            - Evicts least recently used node if cache exceeds limit.
        """
        if key in self.map:
            node=self.map[key] 
            node.value=value  
            self.List.push_head(node=node)
        else:
            if self.count>=self.limit:
                old_key,old_value=self.List.pop_tail()
                del self.map[old_key]
                self.count -=1

            new_node=self.List.push_head(key=key,value=value)
            self.count +=1
            self.map[key]=new_node

  

   