def count_letters(s: str) -> int:
    only_lower = set()
    for letter in s:
        if letter.islower():
            only_lower.add(letter)

    only_upper = set()
    for letter in s:
        if is_upper_case(letter):
            if letter.lower() not in only_lower:
                only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
