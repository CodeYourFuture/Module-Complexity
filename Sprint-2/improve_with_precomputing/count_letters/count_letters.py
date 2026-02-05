from collections import Counter
def count_letters(s: str) -> int:
    #Returns the number of letters which only occur in uppercase in the passed string
    letters = set(s)
    only_upper = 0
    for letter in letters:
        if letter.isupper() and letter.lower() not in letters:
                only_upper += 1
    return only_upper
# Convert the string to a set to remove duplicate characters in O(n)
# Iterate over unique letters and check lowercase membership in O(1)
# Total time complexity: O(n)
# Space complexity: O(u), where u is the number of unique characters