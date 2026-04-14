from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
    Outer loop runs n times (each value in values)
    Inner loop runs up to k times (size of unique_items, worst case k = n)
    Time complexity: O(n^2)
    Space complexity: O(n)
    Optimal time complexity: O(n)
    """
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result
