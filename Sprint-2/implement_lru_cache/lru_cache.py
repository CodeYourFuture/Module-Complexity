import time

our_list = []  
lookup_map = {} 
limit = 0

#  `LruCache(limit)` should construct 
# an LRU cache which never stores more than `limit` entries.
def LruCache(user_limit):
    global limit, our_list, lookup_map
    limit = user_limit
    our_list = []
    lookup_map = {}

# * `set(key, value)` should associate `value` with the passed `key`.
def set(key, value):
    global our_list, lookup_map
    
    if key in lookup_map:
        old_item = lookup_map[key]
        our_list.remove(old_item)
            
    wrapped_item = {
        "key": key,
        "value": value,
        "tracker": time.time()
    }
    
#add to list and map
    our_list.insert(0, wrapped_item)
    lookup_map[key] = wrapped_item
    
#if full remove oldest timestamp so last
    if len(our_list) > limit:
        oldest_item = our_list.pop() 
        
        del lookup_map[oldest_item["key"]]


# * `get(key)` should look-up the value previously associated with `key`.
def get(key):
    global our_list, lookup_map
#check map instead of for loop    
    if key in lookup_map:
        # find by key
        item = lookup_map[key]
        
        # // tracker to now timestamp updaed
        item["tracker"] = time.time()
        
        #move to front
        our_list.remove(item)
        our_list.insert(0, item)
        
        return item["value"]
    return None


#before i did it this was but was looping over each item and did not 
#fit the required complexity
# def get_old(key):
#     for item in our_list: 
#         if item["key"] == key:
#             item["tracker"] = time.time()
#             our_list.remove(item)
#             our_list.insert(0, item)
#             return item["value"]
#     return None

#and before tried with an id not timestamp 
# tracker_number = 0  

# def set(key, value):
#     global tracker_number, our_list, lookup_map
    
   
#     wrapped_item = {
#         "key": key,
#         "value": value,
#         "tracker": tracker_number 
#     }
    
    
#     tracker_number += 1 
    
#     our_list.insert(0, wrapped_item)
#     lookup_map[key] = wrapped_item

# and the loop
# def get_old(key):
#     global tracker_number, our_list
#     for item in our_list: 
#         if item["key"] == key:
#             item["tracker"] = tracker_number
#             tracker_number += 1
            
#             our_list.remove(item)
#             our_list.insert(0, item)
            
#             return item["value"]
#     return None