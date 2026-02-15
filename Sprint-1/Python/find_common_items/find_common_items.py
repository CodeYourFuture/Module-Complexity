from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")



    #Before Reafctoring
"""
    Find common items between two arrays.

    Time Complexity: The function uses a nested loop, where the outer loop runs n times and the inner loop runs m times. 
    This gives O(n * m) time. Inside the inner loop, the expression `i not in common_items` performs 
    a match check on a list of size k, which is O(k). Therefore, the overall worst-case time 
    complexity is O(n * m * k). If both sequences are size n, this becomes O(n^2 * k).

    Space Complexity: We store matching items in a new list `common_items`. If there are k matches, the list uses O(k) 
    space. In the worst case (all items match), this becomes O(n).
    
    Optimal time complexity: O(n+m)-> (Look at each element of the first sequence and the second sequence at least once)
"""
def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:



    common_items = set()   #set has o(1) time complexity
    for i in first_sequence:
        for j in second_sequence:
            if i == j:  #has o(1)
                common_items.add(i) #adding in set has o(1)
    return list(common_items)
#After refactoring we reduce the time complexity to O(n*m) from O(n*m*k)
#Space remain O(k) for the set (worst case O(n)