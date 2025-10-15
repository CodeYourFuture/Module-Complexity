from typing import List
def find_longest_common_prefix(strings: List[str]) -> str:
    if len(strings) < 2:
        return ""
    #Find shortest string limit for prefix
    min_len = min(len(s) for s in strings)
    if min_len == 0:
        return ""
    #Compare character by character across all strings
    for i in range(min_len):
        char_set = set(s[i] for s in strings)
        if len(char_set) > 1:  #mismatch found
            return strings[0][:i]
    return strings[0][:min_len]
#Originally Compares every pair O(n² * m)
#now compare column wise across all strings O(n * m)