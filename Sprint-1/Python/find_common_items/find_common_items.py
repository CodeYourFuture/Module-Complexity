from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: worst O(N1 * N2)
    Space Complexity: worst O(N1 + N2)
    Optimal time complexity: worst become: O(N1 + N2)
    """
    firstSet = set(first_sequence)
    secondSet = set(second_sequence)
    return list(firstSet.intersection(secondSet))
