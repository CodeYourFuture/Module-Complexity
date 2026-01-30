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
    Time Complexity: O(n)
    Space Complexity: O(1)
    Optimal time complexity: O(n)
    """
    running_sum = 0
    running_product = 1

    for number in input_numbers:
        running_sum += number
        running_product *= number

    return {"sum": running_sum, "product": running_product}
