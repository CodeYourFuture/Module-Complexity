def count_letters(s: str) -> int:
    seen = set()
    for letter in s:
        seen.add(letter)

    count = 0
    for letter in seen:
        if is_upper_case(letter) and not letter.lower() in seen:
            count += 1
    return count


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
