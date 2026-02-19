from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


# def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
#     """
#     Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

#     Time complexity:O(n²) Quadratic The outer loop runs n times, and for each value, the inner loop also runs up to n times.
#     Space complexity:O(n) store n elements in worst possible case
#     Optimal time complexity: O(n) can be improved useing set
#     """
#     unique_items = []

#     for value in values:
#         is_duplicate = False
#         for existing in unique_items:
#             if value == existing:
#                 is_duplicate = True
#                 break
#         if not is_duplicate:
#             unique_items.append(value)

#     return unique_items

def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    unique_element= set() # for unique element
    order_element =[] # to order maintain
    for value in values:
        if value not in unique_element:
            unique_element.add(value)
            order_element.append(value)
    return order_element        