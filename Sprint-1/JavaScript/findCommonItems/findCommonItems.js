/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n + m)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const lookup = new Set(secondArray);
  return [...new Set(firstArray.filter(item => lookup.has(item)))];
};