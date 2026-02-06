def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    present_chars = set(s)
    only_upper_count = 0
   
    for char in present_chars:
        if char.isupper():
            if char.lower() not in present_chars:
                only_upper_count += 1
                
    return only_upper_count
