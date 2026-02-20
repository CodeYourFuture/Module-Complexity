from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity:quadratic
    Space complexity:O(N)
    Optimal time complexity:O(N)
    """
    unique_items = []

    # for value in values:
    #     is_duplicate = False
    #     for existing in unique_items:
    #         if value == existing:
    #             is_duplicate = True
    #             break
    #     if not is_duplicate:
    #         unique_items.append(value)

    # return unique_items


    itemsWeChecked = {}
    for item in values:
        if item not in itemsWeChecked:
            unique_items.append(item)
            itemsWeChecked[item] = True
	
    return unique_items