from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    # If the list has less than 2 strings, we can return early (nothing to compare)
    if len(strings) < 2:
        return ""
    #Sort strings to bring similar ones next to each other
    # This helps to find common parts faster without checking every possible pair!
    strings.sort()
    
    longest = ""
   
   #instead of checking all pairs (that is slow), just check each pair of neighbors
    for i in range(len(strings) - 1):
        common = find_common_prefix(strings[i], strings[i + 1])
        if len(common) > len(longest):
            longest = common

    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
