from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:
    there are loops nested that check every pair O(n2) 
    Space Complexity: O(n)
    Optimal time complexity:
     using a set to check numbers seen O(n)
    """
    numbers_seen = set()
    for num in numbers:  # O(n)
        required_num = target_sum - num
        if required_num in numbers_seen:
            return True
        numbers_seen.add(num)
    return False
