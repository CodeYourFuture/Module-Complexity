from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    if not first_sequence or not second_sequence:
        return []

    result_set = set(first_sequence) & set(second_sequence)

    return list(result_set)

# old one have a loop inside a loop for i and for j. If both lists have 10,000 items, that is like 100,000,000 checks

"""
    this function turns both lists into "Sets" to remove duplicates 
     then, it checks each item to find 
    the common elements without using slow nested loops.
    """

"""
Time Complexity (Original): O(N \times M) — The original code used a loop inside a loop (for i and for j). To make it even slower, it also used i not in common_items, which forced the computer to scan a third list. This takes a massive number of steps for large datasets.
Space Complexity (Improved): O(N + M) — The improved version uses extra memory to store the unique items from both sequences inside sets (set_first, set_two, and result_set).
Optimal Time Complexity (Improved): O(N + M) — By turning the sequences into sets, looking up an item with if item in set_two becomes instant. This allows the function to find all common items in a single, fast pass.
"""