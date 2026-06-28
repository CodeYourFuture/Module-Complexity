def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    appeared_upper = set()
    appeared_lower = set()
    for letter in s:
        if not letter.isalpha():
            continue
        if letter.islower():
            appeared_lower.add(letter.lower())
        else:
            appeared_upper.add(letter.lower())
            
    return len(appeared_upper.difference(appeared_lower))


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
