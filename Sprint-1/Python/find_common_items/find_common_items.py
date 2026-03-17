from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n + m) process both sequences
    Space Complexity:O(n + m) two sets are created
    Optimal time complexity:O(n + m) must check all elements
    """
    return list(set(first_sequence).intersection(second_sequence))