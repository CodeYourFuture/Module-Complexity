from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity:
        ANSWER: O(n)
        Because the sequence is looped through once.

    Space complexity:
        ANSWER: O(n)
        Because a set is used to track seen value


    Optimal time complexity:
        ANSWER: O(n)
        Each value is processed once using a set for faster lookup
        
    """
    unique_items = []
    seen = set()


    for value in values:
        if value not in seen:
            seen.add(value) 

            unique_items.append(value)
       

    return unique_items
