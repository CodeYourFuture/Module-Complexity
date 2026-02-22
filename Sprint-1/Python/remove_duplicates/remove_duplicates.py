from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n)
    Space complexity: O(n)
    Optimal time complexity: O(n)
    """
    unique_items = []
    seen = set()

    for value in values:
        if value not in seen:
            unique_items.append(value)
            seen.add(value)

    return unique_items
