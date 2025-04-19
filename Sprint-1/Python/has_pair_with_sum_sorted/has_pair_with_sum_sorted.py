"""
Find if there is a pair of numbers that sum to target. 
Optimise your solution with a precomputation.
Time Complexity: 
Space Complexity:
"""
from typing import List

def has_pair_with_sum_sorted(numbers: List[float], target_sum: float) -> bool:
    sorted_numbers = sorted(numbers)
    left_index = 0
    right_index = len(sorted_numbers) - 1
    
    while left_index < right_index:
        current_sum = sorted_numbers[left_index] + sorted_numbers[right_index]
        if current_sum == target_sum:
            return True
        if current_sum < target_sum:
            left_index += 1
        else:
            right_index -= 1
            
    return False 