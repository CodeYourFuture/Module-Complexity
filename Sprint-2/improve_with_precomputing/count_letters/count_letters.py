def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    seen = set(s)


    """
    Originally had a set "lower" and a set "upper", increment count if item in upper not also in lower
    but this doesn't work with spaces, numeric and other characters.

    This version works better because "1" or space is its own lower case, so when doing the 
    letter.lower() not in seen test, it return false, and the character will not count towards
    the sum of uppercase letters
    """
    return sum(
        1 for letter in seen
        if is_upper_case(letter) and letter.lower() not in seen
    )
    

def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
