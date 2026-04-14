from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n * m)
    Space Complexity: O(n)
    Optimal time complexity: O(n + m)
    Explanation: The function uses a nested loop to check every possible pair of items in the two
    sequences to see if they are common.
    This results in a time complexity of O(n * m).
    Using a set for constant-time lookups can reduce the time complexity to O(n + m)
    by first converting one of the sequences into a set and then checking for common items in a single loop.
    """
    lookup = set(second_sequence)
    result = []
    seen = set()

    for item in first_sequence:
        if item in lookup and item not in seen:
            seen.add(item)
            result.append(item)

    return result
