def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    all_chars_set = set(s)
    upper_set = set(letter for letter in all_chars_set if letter.isupper())
    lower_set = set(letter for letter in all_chars_set if letter.islower())

    only_upper = set()
    for letter in upper_set:
        if letter.lower() not in lower_set:
            only_upper.add(letter)
    return len(only_upper)
#before: it was N^2. It took a for loop and a not in s, which is a loop.
#after: it becomes N + N. The first N is the set created, it can access data instantly. The second N is the for loop.

def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
