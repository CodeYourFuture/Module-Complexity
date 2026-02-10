from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n^2)
    Space complexity: O(n)
    Optimal time complexity: 0(n)
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
    # nested array - O(n^2) complexity

    # here we iterate through the array to make a dict which is O(n) and than convert it to the list which is also O(n)
    return list(dict.fromkeys(values))
