def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    only_upper = 0
    only_uniq = set(s)
    only_uniq_sorted = sorted(only_uniq)
    uppercase = [ch for ch in only_uniq_sorted if ch.isupper()]
    lowercase = [ch for ch in only_uniq_sorted if ch.islower()]
    for i in uppercase:
        if i.lower() not in lowercase:
            only_upper += 1
    return only_upper
