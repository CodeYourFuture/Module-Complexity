from typing import List


def find_longest_common_prefix(strings: List[str]):

    if len(strings) < 2:
        return ""
    
    strings = sorted(strings)
    
    longest = ""
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


"""
The new implementation sorts a string first, then compares each string
with the one that comes after it. On the other hand, the original imple-
mentation compares each string with every single while looping through
nested for loop. 
As a result, the compelxity time drops from the original O(n^2 * m) to
around O(n log n * m).

"""