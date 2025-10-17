from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
    
    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(1) - Only using constant extra space
    Optimal Time Complexity: O(n) - Cannot do better than linear time
    """
    # OPTIMIZED IMPLEMENTATION: O(n) time complexity
    # Previous implementation: O(2n) due to two separate loops
    
    sum_total = 0      # O(1) space
    product = 1   # O(1) space 

    #  O(n) time complexity
    for current_number in input_numbers:
        sum_total += current_number      # O(1) 
        product *= current_number  # O(1) 

    return {"sum": sum_total, "product": product}


# ORIGINAL IMPLEMENTATION (for comparison):
"""
def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum = 0
    for current_number in input_numbers:    # First pass: O(n)
        sum += current_number

    product = 1
    for current_number in input_numbers:     # Second pass: O(n)
        product *= current_number

    return {"sum": sum, "product": product}  # Total: O(2n) = O(n) time

COMPLEXITY ANALYSIS OF ORIGINAL:
- First loop: O(n) iterations to calculate sum
- Second loop: O(n) iterations to calculate product
- Total: O(2n) = O(n) time complexity
- Space: O(1) - only using loop variables

IMPROVEMENTS MADE:
1. Reduced from 2n to n operations (50% fewer iterations)
2. Single pass through list instead of two separate loops
3. Same O(n) time complexity but with better constant factors
"""
