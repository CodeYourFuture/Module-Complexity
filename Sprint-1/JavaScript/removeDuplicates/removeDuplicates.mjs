/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:before refactoring O(n²)- after refactoring O(n)
 * Space Complexity:O(n)
 * Optimal Time Complexity:O(n)
 
 * The original implementation relied on nested loops to detect duplicates,
 *resulting in O(n²) time complexity, which does not scale well for large inputs.
 *The refactored solution uses a Set to perform duplicate checks in constant time.
 *This removes the need for an inner loop and reduces the overall time complexity
 *to O(n), which is optimal for this problem.
 *using  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniqueItemSet = new Set;

  for (let i=0 ;i<inputSequence.length;i++){
    uniqueItemSet.add(inputSequence[i]);
  }
   return [...uniqueItemSet];
}
