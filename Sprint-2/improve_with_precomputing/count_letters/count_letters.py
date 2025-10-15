from collections import Counter
def count_letters(s: str) -> int:
    #Returns the number of letters which only occur in uppercase in the passed string
    letters = Counter(s)  #count occurrences of each character
    only_upper = 0
    for letter in letters:
        if letter.isupper():
            if letter.lower() not in letters:
                only_upper += 1
    return only_upper
#The first implementation was O(n² * m) in the worst case comparing every pair of strings character by character.
# Now,
#Counter scans the string once O(n)
#Checking letter.lower() in letters O(1) per letter
#Total time O(n + u) where u is the number of unique letters