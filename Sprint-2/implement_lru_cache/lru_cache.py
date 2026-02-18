class LruCache:
    def __init__(self,limit) -> None:
        if limit <= 0:           
            raise ValueError("Limit must be greater than zero")
        self.limit = limit #defines a limit, after which before adding anything in our cache we need to remove it
        self.storage = {} #stores data as key value pairs for fast lookups. accessing or updating a key both make it a Most recently used item
        self.order = [] #lRU at index 0, MRU at last index position, tracks usage order 
        pass

#If a key already exists move it to MRU position
    def touch (self,key):
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

# If we want to add or update a key value pair
    def set(self, key, value):
        if key in self.storage:
            self.storage[key] = value  #update the value of the key 
            self.touch(key)
            return
        
#if we are adding a new key and at capacity 
        if len(self.storage) >= self.limit:
            lru_key =self.order.pop(0)
            del self.storage[lru_key]

#Add a new key and set it as MRU
        self.storage[key]= value
        self.touch(key)

    def get(self,key):
            if key not in self.storage:
                return None
            #if it exist set it as used
            self.touch(key)
            return self.storage[key]
    

cache = LruCache(2)
cache.set("a", 1)   # store = {a:1}, order = [a]
cache.set("b", 2)   # store = {a:1,b:2}, order = [a,b]
print(cache.get("a")) # should print 1
cache.get("a")      # returns 1, order = [b,a]  (a is now MRU)
cache.set("c", 3)   # capacity reached, evict LRU = b
cache.get("b")
print(cache.order)                  # store = {a:1,c:3}, order = [a,c]
