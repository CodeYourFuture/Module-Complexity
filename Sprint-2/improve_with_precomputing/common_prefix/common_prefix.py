from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    if len(strings) < 2:
        return ""
    # Precompute: sort the strings so common prefixes are adjacent
    sorted_strings = sorted(strings)
    longest = ""
    for i in range(len(sorted_strings) - 1):
        common = find_common_prefix(sorted_strings[i], sorted_strings[i + 1])
        if len(common) > len(longest):
            longest = common
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
