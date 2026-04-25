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
    Time Complexity: O(2n) = O(n) - We iterate through the list twice (once for sum, once for product)
    Space Complexity: O(1) - Only using constant extra space for variables
    Optimal time complexity: O(n) - We can achieve O(n) by combining both loops into one single pass
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum_value = 0
    product_value = 1
    for current_number in input_numbers:
        sum_value += current_number
        product_value *= current_number

    return {"sum": sum_value, "product": product_value}
