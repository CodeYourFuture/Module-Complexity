from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: The time complexity is O(n + m) because we build a set from the second sequence in O(m) time and iterate through the first sequence in O(n) time.
    Space Complexity: The space complexity is O(n + m) because we store up to all elements of the second sequence in a set and up to the common elements in additional storage. 
    Optimal time complexity: The time complexity is O(n + m) and the space complexity is O(n + m).
    """
    second_set = set(second_sequence)
    seen = set()
    common_items: List[ItemType] = []
    for i in first_sequence:
        if i in second_set and i not in seen:
            seen.add(i)
            common_items.append(i)

    return common_items
