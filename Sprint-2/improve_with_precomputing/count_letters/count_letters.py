def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    uppers = set()
    lowers = set()

    for ch in s:
        if ch.isupper():
            uppers.add(ch)
        elif ch.islower():
            lowers.add(ch)

    count = 0
    for i in uppers:
        if i.lower() not in lowers:
            count += 1
    return count
