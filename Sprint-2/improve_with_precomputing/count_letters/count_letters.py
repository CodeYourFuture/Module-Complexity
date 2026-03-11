def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    only_upper = set()
    
    chars = set(s)  #store all characters once

    for letter in chars:
        if is_upper_case(letter):
            if letter.lower() not in chars:
                only_upper.add(letter)

    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()