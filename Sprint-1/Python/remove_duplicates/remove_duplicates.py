def remove_duplicates(values):

    unique_items = []
    seen = set()

    for value in values:
        if value not in seen:
            unique_items.append(value)
            seen.add(value)

    return unique_items


"""
Remove duplicate values from a sequence,
preserving the order of the first occurrence.

Time complexity: O(n²)
Space complexity: O(n)
Optimal time complexity: O(n)
"""
