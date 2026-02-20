# //operations
# `push_head` should add an element to the start of the list. 
# It should return something that can be passed to `remove` to 
# remove that element in the future.

    

# `pop_tail` should remove an element from the end of the list.
# * `remove` takes a handle from `push_head`, 
# and removes that element from the list.

our_list = []
tracker_number = 0

def push_head(item_to_insert):
# // grab tracker
    global tracker_number
    # //assign so gets updated ///
    id_for_this_particular_item = tracker_number
    # //wrap item to unsert in {}
    wrapped_item = {
        "tracker": id_for_this_particular_item,
        "inserted_item_key": item_to_insert
    }

    our_list.insert(0, wrapped_item)
    tracker_number +=1
    return id_for_this_particular_item

def remove(id_for_this_particular_item):
    for item in our_list:
        if item["tracker"] == id_for_this_particular_item:
            our_list.remove(item)
            return item
        
def pop_tail():
    if len(our_list) > 0:
        return our_list.pop()
            
