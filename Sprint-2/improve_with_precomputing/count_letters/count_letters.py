def count_letters(s: str) -> int:
    upper_letters = set()
    lower_letters = set()

    for letter in s:
        if letter.isupper():
            upper_letters.add(letter)
        elif letter.islower():
            lower_letters.add(letter)

    count = 0
    for letter in upper_letters:
        if letter.lower() not in lower_letters:
            count += 1

    return count