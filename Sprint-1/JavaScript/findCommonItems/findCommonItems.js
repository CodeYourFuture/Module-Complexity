/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n * m) - filter iterates firstArray, includes iterates secondArray
 * Space Complexity: O(n) - Set and result array
 * Optimal Time Complexity: O(n + m) - convert secondArray to Set for O(1) lookups
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  const seen = new Set();
  const result = [];

  for (const item of firstArray) {
    if (secondSet.has(item) && !seen.has(item)) {
      seen.add(item);
      result.push(item);
    }
  }

  return result;
};
