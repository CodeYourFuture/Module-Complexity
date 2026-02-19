from has_pair_with_sum import has_pair_with_sum


def test_has_pair_with_sum_when_pair_exists():
    assert has_pair_with_sum([5, 2, 8, 1, 9], 10) == True
    assert has_pair_with_sum([1, 2, 3, 4], 7) == True


def test_has_pair_with_sum_when_no_pair_exists():
    assert has_pair_with_sum([5, 2, 8, 1, 9], 12) == False


def test_has_pair_with_sum_empty_list():
    assert has_pair_with_sum([], 5) == False
