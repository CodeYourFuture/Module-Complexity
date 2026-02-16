class Node:
    """
    Represents a node in a doubly linked list.
    Each node holds a key-value pair and pointers to the previous and next nodes.
    """
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.previous=None

class LinkedList:
    """
    A doubly linked list supporting:
    - push_head: add a node to the head (most recently used position)
    - pop_tail: remove and return the tail node (least recently used)
    - remove: remove a specific node from the list
    Maintains references to both head and tail nodes for O(1) operations.
    """
    def __init__(self):
        self.head=None
        self.tail=None    
            
    def push_head(self,node=None,key=None,value=None) -> Node:
        """
        Adds a node to the head of the list.
        If 'node' is provided, it is moved to the head.
        If 'node' is None, a new node is created from key and value.
        """
        if node is None:
           new_node=Node(key,value)
        else:
            self.remove(node)
            new_node=node 

        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
           old_head=self.head
           self.head=new_node
           new_node.next=old_head
           old_head.previous=new_node
        new_node.previous=None   
        return new_node
    
    def pop_tail(self) -> any:
        """
        Removes the tail node (least recently used) from the list
        and returns its key and value as a tuple.
        """
        if self.head is None:
            return None
        elif self.head==self.tail:
            node_value=self.head.value
            node_key=self.head.key
            self.head=None
            self.tail=None
        else:
            node_value=self.tail.value
            node_key=self.tail.key
            previous_node=self.tail.previous   
            self.tail=previous_node 
            self.tail.next=None
        return (node_key,node_value)   
    
    def remove(self,node) -> None:
        """
        Removes a specific node from the list.
        Handles nodes at the head, tail, or middle of the list.
        """
        node_to_remove=node
        current_head=self.head
        current_tail=self.tail
        if current_head==current_tail and node_to_remove==current_head:
            #list has only one node
            self.head=None
            self.tail=None
        elif node_to_remove.next is None:
            #Node is the tail
            self.tail=node_to_remove.previous  
            self.tail.next=None  
        elif node_to_remove.previous is None:
            #Node is the head   
            self.head=node_to_remove.next
            self.head.previous=None
        else:
            #Node is in the middle of list
            previous_node=node_to_remove.previous        
            next_node=node_to_remove.next
            previous_node.next=next_node
            next_node.previous=previous_node
        
        node_to_remove.next=None
        node_to_remove.previous=None   

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
        self.List.remove(node)
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
            self.List.remove(node)
            self.List.push_head(node=node)
        else:
            if self.count>=self.limit:
                old_key,old_value=self.List.pop_tail()
                del self.map[old_key]
                self.count -=1

            new_node=self.List.push_head(key=key,value=value)
            self.count +=1
            self.map[key]=new_node

  

   