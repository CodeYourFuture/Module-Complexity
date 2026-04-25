from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time Complexity: O(n²) - where n is the length of the input sequence. For each element in the values sequence,
                     we iterate through all existing items in unique_items to check if it's a duplicate.
                     In the worst case, this requires checking all previous elements.
    Space Complexity: O(k) - where k is the number of unique items. We store up to k items in the unique_items list.
    Optimal time complexity: O(n) - Using a set to track seen items allows us to check for duplicates in O(1) time,
                             reducing the overall complexity from O(n²) to O(n).
    """
    # Optimised approach: Use a set to track seen items for O(1) lookups
    seen_items = set()
    unique_items = []

    for value in values:
        if value not in seen_items:
            seen_items.add(value)
            unique_items.append(value)

    return unique_items
