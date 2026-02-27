from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    Return the longest common prefix shared by any two strings in the list.

    If the list is empty, contains only one string, or no common prefixes
    exist, an empty string is returned.
    """
    if len(strings) < 2:
        return ""

    # Sorting places strings with similar prefixes next to each other.
    # This reduces comparisons from O(n^2) to O(n log n).
    strings.sort()

    longest = ""
    for i in range(len(strings) - 1):
        # Compare only adjacent strings after sorting.
        common = find_common_prefix(strings[i], strings[i + 1])
        if len(common) > len(longest):
            longest = common

    return longest


def find_common_prefix(left: str, right: str) -> str:
    """
    Return the common prefix between two strings.
    """
    min_length = min(len(left), len(right))

    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]

    return left[:min_length]
