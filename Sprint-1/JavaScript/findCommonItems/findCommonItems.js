/**
 * Finds common items between two arrays.
 *
 * Time Complexity:O(n+m) it build set and loop through the first array
 * Space Complexity: O(m) space proportional to size of second array
 * Optimal Time Complexity:O(m+n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
// export const findCommonItems = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
// ];
// Refactored to use a Set for faster lookups, making the code more efficient
export const findCommonItems = (firstArray, secondArray) => {
  const secondArraySet = new Set(secondArray);
  const resultSet = new Set();
  for (const element of firstArray) {
    if (secondArraySet.has(element)) {
      resultSet.add(element);
    }
  }
  return [...resultSet];
};
