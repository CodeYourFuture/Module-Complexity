def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    only_upper = set()

    # Precompute all lowercase letters in the string for faster lookup
    lower_case_set={ch for ch in s if ch.islower() }

    for letter in s:
        if is_upper_case(letter) and letter.lower() not in lower_case_set:
            only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
