from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    if len(strings) < 2:
        return ""
    
    strings.sort()

    longest = ""
    for i in range(len(strings)-1):
        common = find_common_prefix(strings[i], strings[i+1])
        if len(common) > len(longest):
            longest = common
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]

# Complexity for old version code where we hade a nested loop and slicer, and compared every string with other string is
# leading to O(n^2*m+n^2), while on the new script we have complexity sorting O(n log n *m) and comparison O(n*m). Even after using sorting
# which is consuming and costly, the overall complexity is lower because we compare fewer pairs.
# O(n^2*m) and O(n log n *m)