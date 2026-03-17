/**
 * Finds common items between two arrays.
 *
 * Time Complexity:
 *        ANSWER: O(n + m)
          Because both arrays are processed once and we iterate through them to find common elements.

 * Space Complexity: 
          ANSWER: O(n + m)
          because two sets are created
          
 * Optimal Time Complexity:
          ANSWER: O(n + m)
          Because we must check all elements in both arrays (or sets) at least once.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const firstSet = new Set(firstArray);
  const secondSet = new Set(secondArray);

  return [...firstSet.intersection(secondSet)];
};
