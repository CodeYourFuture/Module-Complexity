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
    if not first_sequence or not second_sequence:
        return []

    set_two = set(second_sequence)
    set_first = set(first_sequence)
    result_set = set()

    for item in set_first:
        if item in set_two:
            result_set.add(item)

    return list(result_set)

# old one have a loop inside a loop for i and for j. If both lists have 10,000 items, that is like 100,000,000 checks

"""
    this function turns both lists into "Sets" to remove duplicates 
     then, it checks each item to find 
    the common elements without using slow nested loops.
    """