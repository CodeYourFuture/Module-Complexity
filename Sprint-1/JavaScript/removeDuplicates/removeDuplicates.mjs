/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(n) - Set to track seen elements
 * Optimal Time Complexity: O(n) - Cannot do better than linear time
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  // OPTIMIZED IMPLEMENTATION: O(n) time complexity
  // Previous implementation: O(n²) due to nested loops checking each element

  const seen = new Set(); // O(n)
  const uniqueItems = []; // O(n)

  //  O(n) time complexity
  for (const item of inputSequence) {
    //  O(1) lookup
    if (!seen.has(item)) {
      seen.add(item); // O(1) operation
      uniqueItems.push(item); // O(1) operation
    }
  }

  return uniqueItems;
}
console.log(removeDuplicates([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]));
/*
 * ORIGINAL IMPLEMENTATION (for comparison):
 *
 * export function removeDuplicates(inputSequence) {
 *   const uniqueItems = [];
 *
 *   for (let currentIndex = 0; currentIndex < inputSequence.length; currentIndex++) {
 *     let isDuplicate = false;
 *     for (let compareIndex = 0; compareIndex < uniqueItems.length; compareIndex++) {
 *       if (inputSequence[currentIndex] === uniqueItems[compareIndex]) {
 *         isDuplicate = true;
 *         break;
 *       }
 *     }
 *     if (!isDuplicate) {
 *       uniqueItems.push(inputSequence[currentIndex]);
 *     }
 *   }
 *
 *   return uniqueItems;
 * }
 *
 * COMPLEXITY ANALYSIS OF ORIGINAL:
 * - Outer loop: O(n) iterations through input array
 * - Inner loop: O(k) iterations through uniqueItems array (k grows with each unique element)
 * - Worst case: O(n²) when all elements are unique
 * - Space: O(n) for uniqueItems array
 *
 * PERFORMANCE ISSUES:
 * - Quadratic time complexity O(n²) in worst case
 *
 * IMPROVEMENTS MADE:
 * 1. Reduced from O(n²) to O(n) time complexity
 * 2. Set lookup is O(1) vs linear search O(k)
 * 3. Single pass through input array
 */
