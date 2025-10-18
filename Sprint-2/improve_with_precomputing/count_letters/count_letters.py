def count_letters(text: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # Find all lowercase letters in the string
    lower_set = set(char for char in text if char.islower())
    
    # Find all uppercase letters in the string
    upper_set = set(char for char in text if char.isupper())
    
    # Count uppercase letters that don't have lowercase versions
    only_upper = {char for char in upper_set if char.lower() not in lower_set}
    
    return len(only_upper)
