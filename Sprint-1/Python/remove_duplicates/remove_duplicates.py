from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity:
    Space complexity:
    Optimal time complexity:
    """
    seen = set()
    unique_items = []

    for value in values:
       
        if value not in seen:
            seen.add(value)      
            unique_items.append(value)

    return unique_items

#old code hs a nested loop: for every single value in the original list, you loop through its unique_items list to see if it is already there. For a massive list of 100,000 items, this turns into billions of checks, making the program very slow
"""
    new function does through the list just once. It uses a Set as a 
    quick memory notepad to check if an item is a duplicate. 
    If it's a brand new item, it saves it to the Set and adds it to 
    the result List, keeps everything in original order.
    """
