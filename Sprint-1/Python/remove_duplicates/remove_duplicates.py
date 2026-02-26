from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n2) - nested loop run once per element n times.Same for outer loop
    Space complexity: O(n) - since there's another array to store unique items. its size grow proportionally as the number of unique inputs grow.
    Optimal time complexity:
    """
    # unique_items = []

    # for value in values:
    #     is_duplicate = False
    #     for existing in unique_items:
    #         if value == existing:
    #             is_duplicate = True
    #             break
    #     if not is_duplicate:
    #         unique_items.append(value)

    # return unique_items

    unique_items = []
    checked_values = set()

    for value in values:
        if value not in checked_values:
            unique_items.append(value)
            checked_values.add(value)
    
    return unique_items



   