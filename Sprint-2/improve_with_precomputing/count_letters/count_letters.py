def count_letters(string: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """

    lower_case_set = set()
    upper_case_set = set()
    
    for letter in string:
        if letter.islower():
            lower_case_set.add(letter)
        elif letter.isupper():
            upper_case_set.add(letter)

    count = 0
    for letter in upper_case_set:
       if letter.lower() not in lower_case_set:
        count += 1
    return count

# The Space complexity for new and old script is O(n), but Time complexity the old one is O(n)^2 which is insufficient compare
# to new code Time complexity O(n).


def is_upper_case(letter: str) -> bool:    
    return letter == letter.upper()
