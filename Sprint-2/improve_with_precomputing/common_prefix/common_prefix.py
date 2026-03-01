from typing import List
from functools import lru_cache


def find_longest_common_prefix(strings: List[str]) -> str:
    if len(strings) < 2:
        return ""

    # KEY INSIGHT: sort the strings. The longest common prefix between
    # any two strings must appear between two adjacent strings when sorted.
    # So we only need to check n-1 pairs instead of n² pairs.
    sorted_strings = sorted(strings)

    longest = ""
    for i in range(len(sorted_strings) - 1):
        common = cached_find_common_prefix(sorted_strings[i], sorted_strings[i + 1])
        if len(common) > len(longest):
            longest = common

    return longest


@lru_cache(maxsize=None)
def cached_find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]


def find_common_prefix(left: str, right: str) -> str:
    return cached_find_common_prefix(left, right)