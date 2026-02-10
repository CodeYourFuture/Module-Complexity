from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


# def find_common_items(
#     first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
# ) -> List[ItemType]:
#     """
#     Find common items between two arrays.

#     Time Complexity:
#     Space Complexity:
#     Optimal time complexity:
#     """
#     common_items: List[ItemType] = []
#     for i in first_sequence:
#         for j in second_sequence:
#             if i == j and i not in common_items:
#                 common_items.append(i)
#     return common_items


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n+m)
    Space Complexity: O(m+k)
    Optimal time complexity: O(n+m)
    """
    set_1 = set(first_sequence)
    set_2 = []

    for seq in set_1:
        if seq in second_sequence:
            set_2.append(seq)
    return set_2       



