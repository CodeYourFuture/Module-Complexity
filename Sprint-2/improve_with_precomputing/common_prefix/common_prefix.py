from typing import List


def find_longest_common_prefix(strings: List[str]):
    if len(strings) < 2:
        return ""
    longest = ""
    sorted_strings = list(sorted(strings[:]))
    for i in range(len(sorted_strings) - 1):
        left = sorted_strings[i]
        right = sorted_strings[i + 1]
        common = find_common_prefix(left, right)
        if len(common) > len(longest):
            longest = common
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
