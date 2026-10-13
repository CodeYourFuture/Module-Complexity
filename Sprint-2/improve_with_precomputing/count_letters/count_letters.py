def count_letters(s: str) -> int:
    upper = set()
    lower = set()

    for letter in s:
        if letter.isupper():
            upper.add(letter)
        elif letter.islower():
            lower.add(letter)

    only_upper = upper - {letter.upper() for letter in lower}

    return len(only_upper)