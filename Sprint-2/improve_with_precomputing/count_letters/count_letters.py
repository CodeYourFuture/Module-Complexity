def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    only_lower = set()
    for letter in s:
        if letter.islower():
            only_lower.add(letter)

    only_upper = set()
    for letter in s:
        if letter.isupper():
            if letter.lower() not in only_lower:
                only_upper.add(letter)
    return len(only_upper)