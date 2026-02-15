from typing import Dict, List

#There are two form loops here. Each for loop has a time complexity of o(n)
#Total complexity becomes o(2n), we drop constants in complexity so time complexity is o(n).
# We are only using two varaible sum and product and no additional data structure are created,
# so space complexity is constant at o(1)
# We can refactor the code with one for loop which  will not affect the time or space complexity but is efficient in practise.

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

    sum = 0
    product =1 
    for current_number in input_numbers:
        sum += current_number
        product *= current_number

    return {"sum": sum, "product": product}
