from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return True
    return False


'''
Time Complexity:

Outer loop: i goes from 0 to n-1 = O(n)

Inner loop: j goes from i+1 to n-1 = O(n) (in worst case)

total comparison = n * (n - 1) / 2 

Therefor total complexity = O(n²)

Space Complexity:

not creating new lists, sets, or hash maps. Only using loop variables i, j, and a few constants.

Space Complexity: O(1)
'''


#optimal 


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False

## Optimal for Time complexity. Reduces it to O(n), but increases the space complexity to O(n).