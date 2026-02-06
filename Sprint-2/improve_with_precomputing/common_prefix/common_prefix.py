from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    if len(strings) < 2:
        return ""
    
    strings.sort()
    longest = ""

    for i in range(len(strings) - 1):
        first_string = strings[i]
        second_string = strings[i + 1]
        
        common = find_common_prefix(first_string, second_string)
        
        if len(common) > len(longest):
            longest = common
            
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
