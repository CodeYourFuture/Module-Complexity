from find_common_items import find_common_items


def test_find_common_items_with_common_elements():
    assert find_common_items([10, 20, 30], [20, 30, 40]) == [20, 30]


def test_find_common_items_with_no_common_elements():
    assert find_common_items(["x", "y", "z"], ["a", "b", "c"]) == []


def test_find_common_items_with_empty_list():
    assert find_common_items([], [1, 2, 3]) == []
