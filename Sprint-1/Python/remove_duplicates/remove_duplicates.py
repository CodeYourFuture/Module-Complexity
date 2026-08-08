from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: Outer loop O(n) Inner loop (worst case) O(n) total --->O(n*n)
    Space complexity: We have an array ,unique_items, total --->O(n)
    Optimal time complexity: O(n) using a set for fast lookups
    """
    unique_items = []
    seen = set()
    for value in values: # O(n)
        if value not in seen: # O(1)
            seen.add(value) # O(1)
            unique_items.append(value) # O(1)
    return unique_items
