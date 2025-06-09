/**
 * Finds common items between two arrays.
 *
 * Time Complexity:O(n * m)
 * Space Complexity: O(k) k<=n
 * Optimal Time Complexity: O(n+m+k)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
/*export const findCommonItems = (firstArray, secondArray) => [
  ...new Set(firstArray.filter((item) => secondArray.includes(item))),
];*/

export const findCommonItems = (firstArray, secondArray) => {
  const setSecond = new Set(secondArray); // O(m)
  const seen = new Set();

  for (const item of firstArray) { // )(n)
    if (setSecond.has(item)) {
      seen.add(item);
    }
  }

  return [...seen]; //)(k)
};

