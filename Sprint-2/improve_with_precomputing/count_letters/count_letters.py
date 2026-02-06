def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # Precompute: create set of all lowercase letters in the string (O(n))
    lowercase_letters = set(c for c in s if c.islower())
    
    # Now just count uppercase letters that don't have a lowercase version
    only_upper = set()
    for letter in s:
        if is_upper_case(letter):
            if letter.lower() not in lowercase_letters:
                only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
