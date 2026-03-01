def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    lower_case = set()
    upper_case = set()

    # collects lowercase and uppercase letters
    for letter in s:
        if letter.islower():
            lower_case.add(letter)
        elif is_upper_case(letter):
            upper_case.add(letter)

    # counts uppercase letters not in lowercase
    count = 0
    for letter in upper_case:
        if letter.lower() not in lower_case:
            count += 1

    return count

def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
