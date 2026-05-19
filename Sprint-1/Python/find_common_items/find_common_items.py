from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.
        
    The complexity of the original code was 0( n x m) because for every item in the first_sequence was compared against every item in second_sequence.
    With the new implementation the time complexity is 0(n + m), because one iteration is made to build second_set; then another iteration through first_sequence.

    Time Complexity: The time complexity is O(n + m) 
    Space Complexity: The space complexity is O(n + m) 
    Optimal time complexity: The time complexity is O(n + m) 
    
    """
    second_set = set(second_sequence)
    seen = set()
    common_items: List[ItemType] = []
    for i in first_sequence:
        if i in second_set and i not in seen:
            seen.add(i)
            common_items.append(i)

    return common_items
