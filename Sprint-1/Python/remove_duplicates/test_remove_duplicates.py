from remove_duplicates import remove_duplicates


def test_removes_duplicate_numbers():
    assert remove_duplicates([5, 2, 2, 3, 4, 4, 1]) == [5, 2, 3, 4, 1]


def test_removes_duplicate_strings():
    assert remove_duplicates(["a", "e", "b", "a", "c", "c", "a"]) == [
        "a",
        "e",
        "b",
        "c",
    ]


def test_empty_array():
    assert remove_duplicates([]) == []


def test_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1]) == [1]
