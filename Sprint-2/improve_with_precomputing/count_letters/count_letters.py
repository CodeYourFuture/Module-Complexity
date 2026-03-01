def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # Precompute: build a set of all characters ONCE — lookups are now O(1)
    char_set = set(s)

    only_upper = set()
    for letter in char_set:            # iterate unique chars only, not all 10M
        if is_upper_case(letter):
            if letter.lower() not in char_set:  # O(1) lookup instead of O(n)
                only_upper.add(letter)

    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()