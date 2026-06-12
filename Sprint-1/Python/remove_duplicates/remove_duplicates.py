from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(N*N) quadratic
    Space complexity: O(N)
    Optimal time complexity: become O(N)
    """

    unique_items = []
    for value in values:
        if value not in unique_items:
            unique_items.append(value)

    return unique_items
