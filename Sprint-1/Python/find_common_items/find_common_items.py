from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: Quadratic
    Space Complexity: ON)
    Optimal time complexity: O(N)
    """
    common_items: List[ItemType] = []
    # for i in first_sequence:
    #     for j in second_sequence:
    #         if i == j and i not in common_items:
    #             common_items.append(i)
    # return common_items

    dictToCheck = {}

    for item in first_sequence:
	    	dictToCheck[item] = True
	
    for item in second_sequence:	
           if item in dictToCheck:
                common_items.append(item)
                dictToCheck.pop(item)
	
    return common_items
	
