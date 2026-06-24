/**
 * Finds common items between two arrays.
 *
 * Time Complexity: now is O(n^2) - coz we doing instead loop one with the filter first array then we checking the array with includes loop to find out if the item are common in both arrays 
 * Space Complexity: is O(n) - coz it is grows directly proportional with the input size 
 * Optimal Time Complexity: to O(n), after i used a Set, now the lookup is faster instead of checking the whole second array each time
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  let second = new Set(secondArray)
  return [ ...new Set(firstArray.filter((item) => second.has(item))) ]
}
console.log(findCommonItems([1, 2, 2, 3], [4, 3, 2]))

