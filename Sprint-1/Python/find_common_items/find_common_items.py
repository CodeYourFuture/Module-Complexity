from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(N*M), it is a loop inside a loop
    Space Complexity: O(N), the size of the common_items would grow to N in the worst case
    Optimal time complexity: O(N + M), N is for the firstSet, M is the filter in second
    """
    # common_items: List[ItemType] = []
    # for i in first_sequence:
    #     for j in second_sequence:
    #         if i == j and i not in common_items:
    #             common_items.append(i)
    # return common_items

    return list(set(first_sequence).intersection(second_sequence))

