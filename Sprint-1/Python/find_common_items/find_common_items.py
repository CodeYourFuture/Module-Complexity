from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n + m) - Set creation and intersection 
    Space Complexity:  O(n + m) - Two sets created for the input sequences
    Optimal time complexity: O(n + m) - We must examine each element of both sequences at least once to find common items
    """

    return list(set(first_sequence) & set(second_sequence))


