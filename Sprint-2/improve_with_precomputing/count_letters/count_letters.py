def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # Store all lowercase and uppercase letters from the string
    # This helps to check faster later
    lower_letters = set()
    upper_letters = set()
    
    # Go through the string once and fill the sets
    for letter in s:
        if is_upper_case(letter):
            upper_letters.add(letter)
        else:
            lower_letters.add(letter)
   
    # Only keep uppercase letters that don't have lowercase versions
    # Using sets makes this check much faster
    only_upper = {letter for letter in upper_letters if letter.lower() not in lower_letters}
    
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
