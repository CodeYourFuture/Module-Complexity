/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n + m) where n is the length of the first array and m is the length of the second array. This is because we create a Set from the second array (which takes O(m) time) and then filter the first array (which takes O(n) time). The overall time complexity is linear.
 
 

 * Space Complexity: O(m) where m is the length of the second array. This is because we create a Set from the second array, which requires additional space The space complexity is linear with respect to the size of the second array.
 

* Optimal Time Complexity: O(n + m) because we need to process each element in both arrays at least once to find the common items. The use of a Set allows us to achieve this optimal time complexity.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const bSet = new Set(secondArray); 
 return firstArray.filter((e) => bSet.has(e)); 
}

const arr1 = [2, 3, 5];
const arr2 = [1, 2, 3];
const commonItems = findCommonItems(arr1, arr2);
console.log(commonItems);