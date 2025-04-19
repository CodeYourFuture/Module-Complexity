"""
Find common items between two arrays 
Time Complexity: 
Space Complexity:
"""
from typing import List, TypeVar, Sequence

ItemType = TypeVar('ItemType')

def find_common_items(first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]) -> List[ItemType]:
    common_items: List[ItemType] = []
    for i in first_sequence:
        for j in second_sequence:
            if i == j and i not in common_items:
                common_items.append(i)
    return common_items 