def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # Precompute all lowercase and uppercase letters in the string
    lower_set = set(c for c in s if c.islower())
    upper_set = set(c for c in s if c.isupper())
    # Only count uppercase letters that do not have a lowercase version in the string
    only_upper = {c for c in upper_set if c.lower() not in lower_set}
    return len(only_upper)
