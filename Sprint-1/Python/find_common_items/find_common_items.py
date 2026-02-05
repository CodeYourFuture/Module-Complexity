from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Areas of inefficiency in original version:
    - Nested loops compare every element in first_sequence to every element
    in second_sequence (O(n * m)).

    Time Complexity: O(n + m) avrage
    Space Complexity: O(m + k)
    Optimal time complexity: O(n + m)
    """
    second_set = set(second_sequence)
    common_items: List[ItemType] = []
    seen = set()

    for item in first_sequence:
        if item in second_set and item not in seen:
            seen.add(item)
            common_items.append(item)

    return common_items
