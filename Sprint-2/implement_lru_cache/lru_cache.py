'''
if an item needs to be evicted, the item which was least recently used will be evicted. 
Both setting or getting a value counts as a use.
It should support the following operations. Each operation should have a O(1) worst-case time complexity.
* `LruCache(limit)` should construct an LRU cache which never stores more than `limit` entries.
* `set(key, value)` should associate `value` with the passed `key`.
* `get(key)` should look-up the value previously associated with `key`.
'''

class Node:
    def __init__(self, key, value):
        self.key = key        # store the key
        self.value = value    # store the value
        self.prev = None      # previous node in list
        self.next = None      # next node in list


class LruCache:
    def __init__(self, limit):

        self.limit = limit
        self.data = {}        
        self.first = None     
        self.last = None      

    def set(self, key, value):

        if key in self.data:
            node = self.data[key]
            node.value = value   

            # when node is used, is move to front
            if node != self.first:

                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev

                if node == self.last:
                    self.last = node.prev

                node.prev = None
                node.next = self.first
                self.first.prev = node
                self.first = node

            return

        # create new node when key doesn't exit
        node = Node(key, value)
        self.data[key] = node

        node.next = self.first
        if self.first:
            self.first.prev = node
        self.first = node

        if self.last is None:
            self.last = node

        # remove last when size is bigger than limit 
        if len(self.data) > self.limit:
            old = self.last

            del self.data[old.key]

            self.last = old.prev
            if self.last:
                self.last.next = None

    def get(self, key):

        if key not in self.data:
            return None

        node = self.data[key]

        # moving node to front because was used
        if node != self.first:

            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            if node == self.last:
                self.last = node.prev

            node.prev = None
            node.next = self.first
            self.first.prev = node
            self.first = node

        return node.value