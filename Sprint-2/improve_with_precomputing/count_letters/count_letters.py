def count_letters(s: str) -> int:
   """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    if not s:
        return 0
    
    # Precompute using fixed arrays for maximum performance
    has_upper = [False] * 26
    has_lower = [False] * 26
    
    for char in s:
        code = ord(char)
        if 65 <= code <= 90:  # A-Z
            has_upper[code - 65] = True
        elif 97 <= code <= 122:  # a-z
            has_lower[code - 97] = True
    
    # Count uppercase letters without lowercase counterparts
    count = 0
    for i in range(26):
        if has_upper[i] and not has_lower[i]:
            count += 1
    
    return count