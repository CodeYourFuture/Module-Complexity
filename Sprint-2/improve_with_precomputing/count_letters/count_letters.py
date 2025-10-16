from typing import Set


def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # only_upper = set()
    # for letter in s:
    #     if is_upper_case(letter):
    #         if letter.lower() not in s:
    #             only_upper.add(letter)
    # return len(only_upper)
    uppercase_letters : Set[str] = set()
    lowecase_letters : Set[str] = set()

    # Precompute uppercase and lowercase letters
    for letter in s:
        if is_upper_case(letter):
            uppercase_letters.add(letter)
        elif letter.isalpha():
            lowecase_letters.add(letter)  

    # Count uppercase letters that don't appear in lowercase
    count = 0 
    for letter in uppercase_letters:
        if letter.lower() not in lowecase_letters:    
            count +=1
            
    return count         


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
