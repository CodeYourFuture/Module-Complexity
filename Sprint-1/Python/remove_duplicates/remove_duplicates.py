from typing import List, Sequence, TypeVar
from collections import OrderedDict

ItemType = TypeVar("ItemType")


# def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
#     """
#     Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

#     Time complexity:
#     Space complexity:
#     Optimal time complexity:
#     """
#     unique_items = []

#     for value in values:
#         is_duplicate = False
#         for existing in unique_items:
#             if value == existing:
#                 is_duplicate = True
#                 break
#         if not is_duplicate:
#             unique_items.append(value)

#     return unique_items

def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n)
    Space complexity: O(n)
    Optimal time complexity: O(n)
    """
    return list(OrderedDict.fromkeys(values))

# Used OrderedDict to create a dictionary with the list elements as keys (preserves order)
# Then, convert it back to a list to remove duplicates 
# https://www.w3resource.com/python-exercises/list-advanced/python-list-advanced-exercise-8.php#:~:text=The%20Python%20OrderedDict.,order%20of%20the%20remaining%20elements.
