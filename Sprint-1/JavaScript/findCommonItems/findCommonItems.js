/**
 * Finds unique common items between two arrays.
 *
 * Time Complexity: O(n + m)
 * Space Complexity: O(n + k)
 * Optimal Time Complexity: O(n + m)
 *
 * The original solution used Array.includes(), which searches
 * the second array for every element in the first array.
 * This version converts the second array into a Set so lookups
 * are much faster.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  const commonItems = new Set();

  for (const item of firstArray) {
    if (secondSet.has(item)) {
      commonItems.add(item);
    }
  }

  return [...commonItems];
};
