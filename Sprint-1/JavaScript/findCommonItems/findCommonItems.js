/**
 * Finds common items between two arrays.
 *
 * Time Complexity:
 *        ANSWER: O(n + m)
          Because the second array is converted into a Set once, and the first array is looped through once.

 * Space Complexity: 
          ANSWER: O(n)
          Because a Set is used to store unique common item 
          
 * Optimal Time Complexity:
          ANSWER: O(n + m)
          Possible by using a Set for faster lookup
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);

  return [...new Set(firstArray.filter(item => secondSet.has(item)))];
};
