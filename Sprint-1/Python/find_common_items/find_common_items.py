from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n + m) - Single pass through both sequences
    Space Complexity: O(min(n, m)) - Set size bounded by smaller sequence
    Optimal Time Complexity: O(n + m) - Cannot do better than linear time
    """
    # OPTIMIZED IMPLEMENTATION: O(n + m) time complexity
    # Previous implementation: O(n × m) due to nested loops with linear search
    
    # Convert second sequence to set for O(1) lookup: O(m) time, O(m) space
    second_set = set(second_sequence)
    
    # Find common items using set lookup: O(n) time
    seen_items = set()
    common_items = []
    for item in first_sequence:
        if item in second_set and item not in seen_items:
            common_items.append(item)
            seen_items.add(item)
    
    return common_items


# ORIGINAL IMPLEMENTATION (for comparison):
"""
def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    common_items: List[ItemType] = []
    for i in first_sequence:                    # O(n) iterations
        for j in second_sequence:               # O(m) iterations each
            if i == j and i not in common_items: # O(k) linear search
                common_items.append(i)
    return common_items

COMPLEXITY ANALYSIS OF ORIGINAL:
- Outer loop: O(n) iterations through first_sequence
- Inner loop: O(m) iterations through second_sequence
- Linear search: O(k) for 'i not in common_items' check
- Total: O(n × m × k) time complexity in worst case
- Space: O(n) for common_items list

PERFORMANCE ISSUES:
- Quadratic time complexity O(n × m) from nested loops

IMPROVEMENTS MADE:
1. Reduced from O(n × m × k) to O(n + m) time complexity
2. Set lookup is O(1) vs nested iteration O(m)
3. Single pass through first_sequence
"""
