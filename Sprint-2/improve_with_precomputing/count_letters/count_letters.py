def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    seen = set(s)
    return sum(
        1 for letter in seen
        if is_upper_case(letter) and letter.lower() not in seen
    )

def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
