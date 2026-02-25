/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n * m) - filter checks each element of firstArray and includes scans secondArray
 * Space Complexity: O(n) - filter creates a new array where size grows as the input of matches grows. Same thing with set.
 * Optimal Time Complexity: O(n + m) - each element must be examined at least once; using a Set allows O(1) lookups
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */

// export const findCommonItems = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
// ];



export const findCommonItems = (firstArray, secondArray) => {
  const arrayToSet = new Set(secondArray);
};