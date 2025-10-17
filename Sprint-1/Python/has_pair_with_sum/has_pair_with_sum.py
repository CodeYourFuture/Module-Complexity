from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(n) - Set to store seen numbers
    Optimal Time Complexity: O(n) - Cannot do better than linear time
    """
    # OPTIMIZED IMPLEMENTATION: O(n) time complexity
    # Previous implementation: O(n²) due to nested loops
    
    seen = set()  # O(n) space for storing seen numbers
    
    # Single pass through list: O(n) time complexity
    for num in numbers:
        complement = target_sum - num  
        
        # Check if complement exists in seen numbers: O(1) lookup
        if complement in seen:
            return True  
        
        # Add current number to seen set: O(1) operation
        seen.add(num)
    
    return False  

# ORIGINAL IMPLEMENTATION (for comparison):
"""
def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    for i in range(len(numbers)):           # O(n) iterations
        for j in range(i + 1, len(numbers)): # O(n) iterations each
            if numbers[i] + numbers[j] == target_sum:  # O(1) comparison
                return True
    return False

COMPLEXITY ANALYSIS OF ORIGINAL:
- Outer loop: O(n) iterations
- Inner loop: O(n) iterations for each outer iteration
- Total: O(n²) time complexity
- Space: O(1) - only using loop variables

PERFORMANCE ISSUES:
- Quadratic time complexity O(n²)

IMPROVEMENTS MADE:
1. Reduced from O(n²) to O(n) time complexity
2. Single pass through list instead of nested loops
3. Set lookup is O(1) vs nested iteration O(n)
"""
