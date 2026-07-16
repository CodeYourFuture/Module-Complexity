from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n * m) - nested loops compare every pair
    Space Complexity: O(n) - stores common items in list
    Optimal time complexity: O(n + m) - convert second_sequence to set for O(1) lookups
    """
    second_set = set(second_sequence)
    seen = set()
    common_items: List[ItemType] = []

    for item in first_sequence:
        if item in second_set and item not in seen:
            seen.add(item)
            common_items.append(item)

    return common_items
