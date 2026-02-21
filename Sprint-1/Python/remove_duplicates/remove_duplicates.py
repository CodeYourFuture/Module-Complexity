from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity:
    Space complexity:
    Optimal time complexity:
    """

    """
    The time complexity in the new implementation is O(n) because we only loop and iterated through the array once. The use of set to add and check value for occurrence is O(1) which is the best Optimal time complexity
    """

    unique_items = []
    new_set = set()

    for value in values:

        if value not in new_set:
            unique_items.append(value)
            new_set.add(value)

    return unique_items
