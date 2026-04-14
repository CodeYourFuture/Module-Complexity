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
    Explanation: The function loops through the list of input numbers twice, once to calculate the
    sum and once to calculate the product. The results in O(n n) = O(n) time. It uses only

    Refactor: We can calculate both the sum and product in a single loop,
    which reduces the time complexity to O(n).
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    total_sum = 0
    total_product = 1

    for num in input_numbers:
        total_sum += num
        total_product *= num

    return {"sum": total_sum, "product": total_product}
