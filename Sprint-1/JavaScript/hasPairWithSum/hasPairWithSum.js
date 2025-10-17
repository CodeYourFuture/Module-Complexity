/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(n) - Set to store seen numbers
 * Optimal Time Complexity: O(n) - Cannot do better than linear time
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  // OPTIMIZED IMPLEMENTATION: O(n) time complexity
  // Previous implementation: O(n²) due to nested loops

  const seen = new Set(); // O(n)

  //  O(n) time complexity
  for (const num of numbers) {
    const complement = target - num;
    // O(1) lookup
    if (seen.has(complement)) {
      return true;
    }

    //  O(1) operation
    seen.add(num);
  }
  return false;
}
console.log(hasPairWithSum([3, 2, 3, 4, 5], 9));
/*
 * ORIGINAL IMPLEMENTATION (for comparison):
 *
 * export function hasPairWithSum(numbers, target) {
 *   for (let i = 0; i < numbers.length; i++) {           // O(n) iterations
 *     for (let j = i + 1; j < numbers.length; j++) {     // O(n) iterations each
 *       if (numbers[i] + numbers[j] === target) {       // O(1) comparison
 *         return true;
 *       }
 *     }
 *   }
 *   return false;
 * }
 *
 * COMPLEXITY ANALYSIS OF ORIGINAL:
 * - Outer loop: O(n) iterations
 * - Inner loop: O(n) iterations for each outer iteration
 * - Total: O(n²) time complexity
 * - Space: O(1) - only using loop variables
 *
 * PERFORMANCE ISSUES:
 * - Quadratic time complexity O(n²)
 *
 * IMPROVEMENTS MADE:
 * 1. Reduced from O(n²) to O(n) time complexity
 * 2. Single pass through array instead of nested loops
 * 3. Set lookup is O(1) vs nested iteration O(n)
 */
