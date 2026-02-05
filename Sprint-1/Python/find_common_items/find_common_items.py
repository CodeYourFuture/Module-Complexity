from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n)
    The old code used nested loops (loop inside a loop), which is slow O(n^2).
    I converted the lists to Sets. Finding the intersection of two sets is linear time O(n).

    Space Complexity: O(n) - We create a new set to store the items for comparison.
    Optimal time complexity: O(n) - We must read the input lists at least once to compare them.
    """

    # Refactor: I used Python Sets.
    # set(first_sequence) & set(second_sequence) finds common items instantly.
    return list(set(first_sequence) & set(second_sequence))
