from typing import List

def find_longest_common_prefix(strings: List[str]) -> str:
    """
    Returns the longest string common at the start of any two strings in the list.
    """
    if len(strings) < 2:
        return ""

    # Precompute the set of prefixes for each string
    prefixes = {}
    for s in strings:
        prefixes[s] = [s[:i] for i in range(1, len(s) + 1)]

    longest = ""
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            # Compare prefixes of strings[i] and strings[j] efficiently
            common = _common_prefix_precomputed(prefixes[strings[i]], strings[j])
            if len(common) > len(longest):
                longest = common

    return longest

def _common_prefix_precomputed(prefix_list: List[str], other: str) -> str:
    # Find the longest prefix of other that exists in prefix_list
    for prefix in reversed(prefix_list):
        if other.startswith(prefix):
            return prefix
    return ""
