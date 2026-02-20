from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:Quadratic   
    Space Complexity:O(N)
    Optimal time complexity:O(N)
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return True
    return False
    # // i am using my cake exqmple from js 
    inventory_of_slices = {}

    for slice in numbers:
        missing_piece = target_sum - slice
        if missing_piece in inventory_of_slices:
            return True

        inventory_of_slices[slice] = True

    return False