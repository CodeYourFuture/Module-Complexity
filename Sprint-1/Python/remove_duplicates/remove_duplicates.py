from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity:
    Space complexity:
    Optimal time complexity:
    """
    unique_items = []

    for value in values:
        is_duplicate = False
        for existing in unique_items:
            if value == existing:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_items.append(value)

    return unique_items


"""
Time Complexity:

1 + 2 + 3 + ... + (n - 1) = n(n - 1)/2 = O(n²)

Space Complexity:

Even though we're just using .append(), the list grows linearly, so it is s O(n) space.

"""

#Optimal Solution

def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    seen = set()
    unique_items = []
    
    for value in values:
        if value not in seen:
            seen.add(value)
            unique_items.append(value)
    
    return unique_items

'''
Time Complexity: O(n)
Space Complexity: O(n) storing unique_items and seen
'''