from typing import List, Sequence, TypeVar


ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n^3): we effectively have three nested loops - the first over first_sequence, the second over second_sequence, and the third in the "not in" check which may contain the same number of elements as either of the sequences.
    Space Complexity: O(n): in the case of complete overlap we may store all of the elements from the sequences in common_items.
    Optimal time complexity: We could optimise this to O(n) by using data structures with O(1) insertion and contains look-up.
    """
    common_items: Set[ItemType] = set()

    second_set = set(second_sequence)
    for i in first_sequence:
        if i in second_set:
            common_items.add(i)

    return list(common_items)
