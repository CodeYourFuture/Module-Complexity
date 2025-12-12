from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """

    if not strings or len(strings) < 2:
        return ""

    # Precompute sorted strings
    sorted_strings = sorted(strings)
    longest = ""

    for i in range(len(sorted_strings) - 1):
        s1, s2 = sorted_strings[i], sorted_strings[i + 1]
        # Find common prefix between them
        prefix_len = 0
        max_len = min(len(s1), len(s2))
        while prefix_len < max_len and s1[prefix_len] == s2[prefix_len]:
            prefix_len += 1
        if prefix_len > len(longest):
            longest = s1[:prefix_len]

    return longest
