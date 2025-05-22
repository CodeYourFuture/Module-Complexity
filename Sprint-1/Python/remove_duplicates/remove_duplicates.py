from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n^2) - Two nested loops, each looking over worst-case the whole input list.
    Space complexity: O(n) - Stores the overlapping items, which may be proportional to all of them.
    Optimal time complexity: O(n) - If we use a data structure with O(1) insertion and contains-look-up to track which elements have already been seen.
    """
    unique_items = set()
    # Python sets don't preserve insertion order, so we need to separately track the correct order.
    # Use the set to gate adding but the list for keeping them in the correct order.
    ordered_items = []

    for value in values:
        if value not in unique_items:
            unique_items.add(value)
            ordered_items.append(value)

    return ordered_items
