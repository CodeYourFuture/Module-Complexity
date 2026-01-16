from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n)
    The old code checked the list repeatedly, which is O(n^2).
    I used a 'Set' to remember seen items for O(1) lookups, while appending to a list to keep the order.

    Space Complexity: O(n) - We use a Set to store seen items and a List for the result.

    Optimal time complexity: O(n) - We must iterate through the input at least once.
    """

    # Refactor: I used a Set to track items we have seen because checking a Set is O(1).
    # I also used a List to build the result so we keep the original order.
    seen = set()
    unique_items = []

    for value in values:
        # Check if we have seen this value before.
        if value not in seen:
            unique_items.append(value)
            seen.add(value)

    return unique_items
