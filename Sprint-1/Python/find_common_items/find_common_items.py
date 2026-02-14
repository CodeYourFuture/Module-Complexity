from typing import List,  TypeVar

ItemType = TypeVar("ItemType")

# Original version: O(n × m) due to nested loops
# Refactored version: O(n + m) using a set for constant-time lookups
# This is optimal and cannot be further reduced because all input
# elements must be processed at least once.
# use this link :https://www.w3schools.com/python/ref_set_intersection.asp

def find_common_items(
    first_sequence, second_sequence
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity:O(n + m)
    Space Complexity:O(n + m)
    Optimal time complexity:O(n + m)
    """
    second_set=set(second_sequence)
    first_set=set(first_sequence)
    common_set=first_set.intersection(second_set)
    return list(common_set)
