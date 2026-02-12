from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.
    Time Complexity: O(n * m * k) in the worst case, where:
    - n = length of first_sequence (outer loop)
    - m = length of second_sequence (inner loop)
    - k = length of common_items, because "i not in common_items" requires scanning this list

    Space Complexity:In first implementation We only store the common items in a new list.--> O(n)


    Optimal time complexity:This can be improved to O(n + m) by using a set for faster lookups.
    """
    first_set=set(first_sequence) # O(n)
    commons=[item for item in second_sequence if item in first_set] # O(m)
    return list(set(commons)) # remove duplicates
