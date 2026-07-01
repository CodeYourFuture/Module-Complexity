def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    letters = set(s)
    only_upper = set()
    
    for letter in s:
        if letter.isupper():
            if letter.lower() not in letters:
                only_upper.add(letter)
    return len(only_upper)
