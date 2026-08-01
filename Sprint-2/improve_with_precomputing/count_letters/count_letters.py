def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case 
    in the passed string.
    """
    
    lowercase_set = set(letter for letter in s if letter == letter.lower())
    
    only_upper = set()
    for letter in s:
        if is_upper_case(letter):
            if letter.lower() not in lowercase_set:  # O(1) lookup instead of O(n)
                only_upper.add(letter)
    return len(only_upper)

def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()