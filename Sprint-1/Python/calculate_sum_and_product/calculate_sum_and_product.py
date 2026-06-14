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
    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    total_sum = 0
    total_product = 1
    for current_number in input_numbers:
        total_sum += current_number
        total_product *= current_number

    return {"sum": total_sum, "product": total_product}

# in the old code we have two separate loops that run one after the other. If the list has 10,000 numbers, the first loop runs 10,000 times to calculate the sum, and the second loop runs 10,000 times to calculate the product
# in the new code we use only one loop which will be doing same job by working half of the old code
# if input_numbers is a small array you may dont see a diffirent but if it is a massive array then you will see it is much faster
# sum is a built-in function name, it is safer to use a name like total_sum so Python doesnt get confused

"""
Time Complexity (Original): O(N) — The original code is fast because it uses two separate loops that run one after the other. It loops through the list once for the sum, and then loops through it a second time for the product.
Space Complexity (Improved): O(1) — The improved version uses constant memory. It only tracks a couple of simple numbers (total_sum and total_product), which takes up the same tiny amount of space no matter how big the list grows.
Optimal Time Complexity (Improved): O(N) — The improved version is still linear time, but it is better because it combines everything into a single loop. It does all the math in just one single pass through the list.
"""
