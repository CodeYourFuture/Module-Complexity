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
    Time Complexity:There are two separate loops O(n)+O(n) total --->O(n)
    Space Complexity:We have two variables sum and product O(1) total --->O(1)
    Optimal time complexity: O(n) cannot be improved because we need to process each element at least once
    but the code can be refactored for better readability.
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum = 0
    product = 1
    for current_number in input_numbers:
        sum += current_number
        product *= current_number
    return {"sum": sum, "product": product}
