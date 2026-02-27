def count_letters(s: str) -> int:
   
    lower_letters = {letter for letter in s if letter.islower()}
    only_upper = set()
    for letter in s:
        if is_upper_case(letter):
            if letter.lower() not in lower_letters:
                only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
