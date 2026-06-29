def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    lowercase_letters = {letter.lower() for letter in s if letter.islower()}

    only_upper = set()
    for letter in s:
        if letter.isupper() and letter.lower() not in lowercase_letters:
            only_upper.add(letter)
    return len(only_upper)


# Before: O(n^2) for each uppercase letter, we checked if the lowercase form was in the string s itself, an O(n) scan repeated per letter.
# After: precompute a set of lowercase letters seen in 's' once (O(n)), so each presence check becomes O(1), making the overall complexity O(n).
