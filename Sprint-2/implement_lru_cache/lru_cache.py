from linked_list import LinkedList, Node

class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be positive")
        self.limit = limit
        self.dict = {}
        self.linked_list = LinkedList()

    def get(self, key):
        if key not in self.dict:
            return None
        else:
            most_recent_node = self.linked_list.remove(self.dict[key])
            self.linked_list.push_head(most_recent_node)
            return most_recent_node.value
        
    def set(self, key, value):
        if key in self.dict:
            self.dict[key].value = value
            self.get(key)
        else:
            if len(self.dict) == self.limit:
                removed_node = self.linked_list.pop_tail()
                del self.dict[removed_node.key]
            self.dict[key] = Node(key, value)
            self.linked_list.push_head(self.dict[key])
        
