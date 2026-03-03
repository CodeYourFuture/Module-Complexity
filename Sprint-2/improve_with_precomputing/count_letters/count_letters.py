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



"""
The old implementation scans through the entire string for every uppercase letter
we check against, therefore complexity in the worst case is O(n^2). However, in the
new implementation the lowercase letters a store beforehand in a set. This allows
checking against every uppercase letter without scanning through the entire string.
As a result, the complexixty time goes down to O(n) with the new implementation.

"""
