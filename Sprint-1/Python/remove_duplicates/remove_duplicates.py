from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time Complexity: O(n) - Single pass through the sequence
    Space Complexity: O(n) - Set to track seen elements
    Optimal Time Complexity: O(n) - Cannot do better than linear time
    """
    # OPTIMIZED IMPLEMENTATION: O(n) time complexity
    # Previous implementation: O(n²) due to nested loops checking each element
    
    seen = set()  # O(n) 
    unique_items = []  # O(n) 
    
    #  O(n) time complexity
    for value in values:
        #  O(1) lookup
        if value not in seen:
            seen.add(value)  # O(1) 
            unique_items.append(value)  # O(1) 
    
    return unique_items


# ORIGINAL IMPLEMENTATION (for comparison):
"""
def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    unique_items = []

    for value in values:                    # O(n) iterations
        is_duplicate = False
        for existing in unique_items:       # O(k) iterations (k grows with unique elements)
            if value == existing:           # O(1) comparison
                is_duplicate = True
                break
        if not is_duplicate:
            unique_items.append(value)      # O(1) operation

    return unique_items

COMPLEXITY ANALYSIS OF ORIGINAL:
- Outer loop: O(n) iterations through values
- Inner loop: O(k) iterations through unique_items (k grows with each unique element)
- Worst case: O(n²) when all elements are unique
- Space: O(n) for unique_items list

PERFORMANCE ISSUES:
- Quadratic time complexity O(n²) in worst case

IMPROVEMENTS MADE:
1. Reduced from O(n²) to O(n) time complexity
2. Set lookup is O(1) vs linear search O(k)
3. Single pass through input sequence
"""
