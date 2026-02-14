/**
 * Finds common items between two arrays.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
// export const findCommonItems = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
// ];


export const findCommonItems = (firstArray, secondArray) => {

  // In this case, the time complexity is O(n * m), it will only become O(n^2) when the two arrays have equal lengths. This case easily be avoided by using a set to store the second sequence. When checking for a match in the set using item in second-set, this has a time complexity of O(1).

  const set = new Set(secondArray);

  return [... new Set(firstArray.filter(item => set.has(item)))]
}