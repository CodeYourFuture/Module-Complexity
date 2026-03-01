from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    common_items: List[ItemType] = []
    second_sequence_set = set(second_sequence)

    for i in first_sequence:
        if i in second_sequence_set and i not in common_items:
            common_items.append(i)

    return common_items