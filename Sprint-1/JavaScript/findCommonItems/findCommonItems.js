/**
 * Finds common items between two arrays.
 *
 * Time Complexity: worst O(N1 * N2)
 * Space Complexity: worst O(N1 + N2)
 * Optimal Time Complexity: worst become: O(N1 + N2)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const firstSet = new Set(firstArray);
  const secondSet = new Set(secondArray);
  secondArray = [...secondSet].filter((element) => firstSet.has(element))
  return secondArray;
};
