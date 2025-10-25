def count_letters(s: str) -> int:
    """
    Returns the number of letters which only occur in upper case in the passed string.
    """
    # Precompute sets of lowercase and uppercase letters in the string
    lower_letters = {c for c in s if c.islower()}
    upper_letters = {c for c in s if c.isupper()}

    # Count letters that appear only in uppercase
    only_upper = {c for c in upper_letters if c.lower() not in lower_letters}
    return len(only_upper)
