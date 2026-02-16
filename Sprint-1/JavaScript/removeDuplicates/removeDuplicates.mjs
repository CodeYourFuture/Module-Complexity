
 /**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence.
 *
 * Time Complexity:
 *   Before refactoring: O(n^2)
 *   The original solution used nested loops to check for duplicates.
 *   After refactoring: O(n)
 *   Using a Set allows duplicate checks in constant time (O(1)),
 *   removing the need for the inner loop.
 *
 * Space Complexity:
 *   Before refactoring: O(n)
 *   The result array could store up to n unique items.
 *   After refactoring: O(n)
 *   The Set and the final array both store up to n unique items.
 *
 * Optimal Time Complexity:
 *   O(n) — You must inspect each element at least once, and Set lookups are O(1).
 * 
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniques =new Set() //does dupliacte check in O(1)

  for (let i=0 ;i<inputSequence.length;i++){ // O(n)
    uniques.add(inputSequence[i]);
  }
  return Array.from(uniques);
}