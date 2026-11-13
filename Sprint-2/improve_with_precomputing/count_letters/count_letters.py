def count_letters(text: str) -> int:
    """count_letters returns the number of distinct upper case letters that do not appear in lowercase in text"""
    seen = set(text)
    return sum(
        1 for letter in seen
        if is_upper_case(letter) and letter.lower() not in seen
    )

def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
