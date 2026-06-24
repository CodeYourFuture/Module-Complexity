def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    upper_letters = set()
    lower_letters = set()
    for letter in s:
        if letter.isupper():
            upper_letters.add(letter)
        elif letter.islower():
            lower_letters.add(letter)
    
    only_upper_count = 0
    for letter in upper_letters:
        if letter.lower() not in lower_letters:
            only_upper_count += 1
            
    return only_upper_count
