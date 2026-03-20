from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Areas of inefficiency in original version:
    - Nested loops -> O(n * m)

    Time Complexity: O(n + m) avrage
    Space Complexity: O(n + m)
    Optimal time complexity: O(n + m)
    """
    return list(set(first_sequence) & set(second_sequence))
