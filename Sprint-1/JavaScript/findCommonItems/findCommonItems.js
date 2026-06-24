/**
 * Finds common items between two arrays.
 *
 * Initial code has this and can be refactored for optimisation
 * Time Complexity: O(nm)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n + m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
// export const findCommonItems = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
// ];
// The initial solution had an expensive operation of .includes(item) search on the secondArray, resulting in O(nm) time complexity. The optimised code stores the secondArray in a set and allows O(1) lookup and reduce the complexity to O(n+m)
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);

  return [...new Set(firstArray.filter((item) => secondSet.has(item)))];
};
