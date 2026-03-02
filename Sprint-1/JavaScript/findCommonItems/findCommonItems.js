/**
 * Finds common items between two arrays.
 *
 * Initial Time Complexity: O(n × m) [filter with includes]
 * Space Complexity: O(n + m)
 * Optimal Time Complexity: O(n + m) [with Set]
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
