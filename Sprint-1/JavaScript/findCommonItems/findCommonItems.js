/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n + m) - Single pass through both arrays
 * Space Complexity: O(min(n, m)) - Set size bounded by smaller array
 * Optimal Time Complexity: O(n + m) - Cannot do better than linear time
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  // OPTIMIZED IMPLEMENTATION: O(n + m) time complexity
  // Previous implementation: O(n × m) due to nested includes() calls

  // Convert second array to Set for O(1) lookup: O(m) time, O(m) space
  const secondSet = new Set(secondArray);

  // Find common items using Set lookup: O(n) time
  const commonItems = firstArray.filter((item) => secondSet.has(item));

  // Remove duplicates: O(n) time in worst case
  return [...new Set(commonItems)];
};

/*
 * ORIGINAL IMPLEMENTATION (for comparison):
 *
 * export const findCommonItems = (firstArray, secondArray) => [
 *   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
 * ];
 *
 * COMPLEXITY ANALYSIS OF ORIGINAL:
 * - firstArray.filter(): O(n) iterations
 * - secondArray.includes(): O(m) for each iteration
 * - Total: O(n × m) time complexity
 * - Space: O(n) for Set creation
 *
 
 * IMPROVEMENTS MADE:
 * 1. Reduced from O(n × m) to O(n + m) time complexity
 * 2. Set lookup is O(1) vs Array.includes() O(m)
 * 3. Significant performance gain for large arrays
 * 4. Same functionality with better algorithmic efficiency
 
 */
