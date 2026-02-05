from typing import List, Sequence, TypeVar, Set

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
    Refactored to use a set for O(1) average time lookups, achieving O(N) overall time complexity.

    Time complexity: O(N)
    Space complexity: O(N)
    Optimal time complexity: O(N)
    """
    seen: Set[ItemType] = set()
    unique_items: List[ItemType] = []

    for value in values:
        if value not in seen:
            seen.add(value)
            unique_items.append(value)

    return unique_items

""" 
Explanation:
The inner loop performs a linear scan through the unique_items list to check for duplicates, which is the source of the high time complexity.

The only effective way to reduce O(N^2) complexity for this problem is to replace the 
linear search (for existing in unique_items) with an O(1) average time lookup, 
which requires a hash set (set in Python).The optimal approach is to use a set to track seen items, achieving O(N)$ time complexity.

Resource: https://www.w3schools.com/python/ref_set_intersection.asp

"""