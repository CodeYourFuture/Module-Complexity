from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: worst O(N!) - factorial
    Space Complexity: O(numbers.length)
    Optimal time complexity: worth become O(N)
    """
    num_set = set(numbers)
    complements_set = set()
    for i in range(len(numbers)):
        complements_set.add(target_sum - numbers[i])
    intersection = num_set.intersection(complements_set)
    if len(intersection) > 0:
        return True
    return False
