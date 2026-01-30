from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n) - nested loop
    Space Complexity: O(n)
    Optimal time complexity: O(n)
    """
    return list(set(first_sequence) & set(second_sequence))
