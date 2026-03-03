from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: for each element in first_sequence, is compared against every element in second_sequence.  
    Space Complexity: O(the number of unique common elements) 
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
