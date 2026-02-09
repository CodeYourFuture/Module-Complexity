from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: Single pass through the list of numbers, O(n), where n is the number of elements in the input list. Each lookup in the set is O(1) on average, so the overall time complexity is O(n).
    Space Complexity: Set stores up to n elements in the worst case (if all numbers are unique), so the space complexity is O(n).
    Optimal time complexity: 0(n) - We must examine each element at least once to determine if a pair exists that sums to the target, so O(n) is the best we can achieve for this problem.
    """

    """seen is a set that will store the numbers we have already seen as we iterate through the list. 
    For each number, we calculate its complement (the value needed to reach the target sum) 
    and check if that complement is in the seen set. If it is, we have found a pair that sums to the target 
    and can return True. If not, we add the current number to the seen set and continue iterating.
     If we finish iterating through the list without finding a pair, we return False."""

    seen = set() 
    
    for num in numbers:
        complement = target_sum - num
        
        if complement in seen: 
            return True
        
        seen.add(num)
    
    return False