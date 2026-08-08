/**
 * Finds common items between two arrays.
 *
 * Time Complexity:O(n+m) it build set and loop through arrays once
 * Space Complexity: store second array in set
 * Optimal Time Complexity:O(m+n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */

// Refactored to use a Set for faster lookups, making the code more efficient
export const findCommonItems = (firstArray, secondArray) => {
  const setB = new Set(secondArray);
  const common = new Set();

  for (const item of firstArray) {
    if (setB.has(item)) {
      common.add(item);
    }
  }

  return [...common];
};

