from calculate_sum_and_product import calculate_sum_and_product


def test_calculate_sum_and_product():
    assert calculate_sum_and_product([1, 2, 3, 4]) == {"sum": 10, "product": 24}
    assert calculate_sum_and_product([-1, 2, -3, 4]) == {"sum": 2, "product": 24}
    assert calculate_sum_and_product([2, 2, 2]) == {"sum": 6, "product": 8}


def test_calculate_sum_and_product_empty_list():
    assert calculate_sum_and_product([]) == {"sum": 0, "product": 1}
