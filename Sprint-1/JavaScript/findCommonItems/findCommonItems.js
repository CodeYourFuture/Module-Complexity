/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(N*M), for each item of loop in the firstArray, it has to loop through the secondArray in the worst case
 * Space Complexity: O(N), the worst case is the length of the firstArray
 * Optimal Time Complexity: O(N + M), N is for the Set of firstArray, and M is the loop for secondArray. O(N+M) is better than O(N*M). 
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
// export const findCommonItems = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
// ];

export const findCommonItems = (firstArray, secondArray) => {
  const firstSet = new Set(firstArray);

  const commonInSecond = secondArray.filter((item) => firstSet.has(item));

  return [... new Set(commonInSecond)];
}