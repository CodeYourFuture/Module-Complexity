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

    """ In this case, the time complexity is O(n * m), it will only become O(n^2) when the two arrays have equal lengths. This case easily be avoided by using a set to store the second sequence. When checking for a match in the set using item in second-set, this has a time complexity of O(1).

    """
    
    second_set = set(second_sequence)
    common_items = []

    for item in first_sequence:

        if item in second_set:
            common_items.append(item)
    return common_items
