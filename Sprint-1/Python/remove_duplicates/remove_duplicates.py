from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n^2) - inner loop checks all unique items for each element
    Space complexity: O(n) - stores unique items in list
    Optimal time complexity: O(n) - using a set for O(1) lookups
    """
    seen = set()
    unique_items = []

    for value in values:
        if value not in seen:
            seen.add(value)
            unique_items.append(value)

    return unique_items
