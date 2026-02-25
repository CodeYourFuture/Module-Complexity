def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    chars = set(s)  # precompute all characters once

    only_upper = set()
    for letter in chars:  # iterate unique characters only
        if letter.isupper() and letter.lower() not in chars:
            only_upper.add(letter)

    return len(only_upper)