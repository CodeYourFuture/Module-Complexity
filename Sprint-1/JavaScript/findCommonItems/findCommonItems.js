/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n + m)
 * Space Complexity: O(n + m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */

export function findCommonItems(firstArray, secondArray) {
  const firstSet = new Set(firstArray);
  const secondSet = new Set(secondArray);

  return [...firstSet.intersection(secondSet)];
}
