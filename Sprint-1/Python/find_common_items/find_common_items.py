from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n * m) - where n is the length of the first array and m is the length of the second array.
                     We iterate through each element in the first array and for each element, we check if it exists
                     in the second array using the 'in' operator, which takes O(m) time. We also check if the item
                     is already in common_items using 'not in', which takes O(k) time where k is the size of common_items.
    Space Complexity: O(k) - where k is the number of common items found. We store each common item in the list.
    Optimal time complexity: O(n + m) - Using a hash set (dictionary/set) for the second sequence allows us to achieve
                             linear time by avoiding the nested loop. This reduces the lookup from O(m) to O(1).
    """
    # Create a set from the second sequence for O(1) lookups
    second_set = set(second_sequence)
    common_items: List[ItemType] = []

    for item in first_sequence:
        if item in second_set and item not in common_items:
            common_items.append(item)

    return common_items
