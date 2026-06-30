from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(N*N) quadratic
    Space complexity: O(N)
    Optimal time complexity: become O(N)
    """
    added_values = set()
    result = []
    for value in values:
        if value not in added_values:
            added_values.add(value)
            result.append(value)

    return result
