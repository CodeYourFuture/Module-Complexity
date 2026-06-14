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

"""
Time Complexity (Original): O(N^2) — The original code used a loop inside a loop (for value and for existing). For every single item in the original list, it had to scan through the unique_items list one-by-one to check for copies, which makes it very slow for big data.
Space Complexity (Improved): O(N) — The improved version uses extra memory to store items inside both a seen set and a unique_items list.
Optimal Time Complexity (Improved): O(N) — By using a set, checking if value not in seen is instant. The computer now flattens out all duplicates in just one single pass while perfectly keeping the original order of the items.
"""
