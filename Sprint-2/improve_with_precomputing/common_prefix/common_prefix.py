from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    longest = ""
    sorted_string = sorted(strings)

    for i in range(len(sorted_string) - 1):
        common = find_common_prefix(
            sorted_string[i], sorted_string[i + 1]
        )
        if len(common) > len(longest):
            longest = common
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]


# Before: the logic force all-pairs comparison, and that results in O(n^2 * m) where n is the number of strings and m is the average string length.
# After: I sort once, then compare only with adjacent pairs, improving it to O(n log n * m).
