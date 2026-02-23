def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    lower_case = set()
    upper_case= set()


## Precompute lowercase and uppercase letters
    for letter in s:
        if letter.islower():
            lower_case.add(letter)
        elif letter.isupper():
            upper_case.add(letter)


# Count uppercase letters whose lowercase version never appears
    count = 0
    for letter in upper_case:
        if letter.lower() not in lower_case:
            count += 1
    return count


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()

#The original solution was O(n²) because it repeatedly checked membership in the full string.
#By precomputing lowercase and uppercase sets, membership checks become O(1), so the whole function becomes O(n).