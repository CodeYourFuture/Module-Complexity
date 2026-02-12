from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: We have nested loop --> O(n*n)
    Space Complexity:We have variables -->O(1)
    Optimal time complexity:We can use only one loop -->O(n)
    """
    seen = set()
    for num in numbers:
        if target_sum - num in seen:
            return True
        seen.add(num)
    return False
