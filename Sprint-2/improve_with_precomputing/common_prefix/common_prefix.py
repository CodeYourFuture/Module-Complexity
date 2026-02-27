from typing import List


def find_longest_common_prefix(strings: List[str]):
  
    if len(strings) < 2:
        return ""

    sorted_strings = sorted(strings)
    longest = ""
    for index in range(len(sorted_strings) - 1):
        common = find_common_prefix(sorted_strings[index], sorted_strings[index + 1])
        if len(common) > len(longest):
            longest = common
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
