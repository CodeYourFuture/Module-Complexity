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


#sets can tell common items directly
def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    first_set = set(first_sequence) #O(n)
    second_set = set(second_sequence) #O(m)

    common_items_set = first_set & second_set # O(min(n,m))  work done is proportional to the size of the smaller set.

    return list(common_items_set)


# Time complexity: reduced with this refactor to optimal O(n+m)
#Space Complexity: O(n + m)- because we create two sets of these sizes.