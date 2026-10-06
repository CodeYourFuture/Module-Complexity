/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n2)
 * Space Complexity: O(n)
 * Optimal Time Complexity:O(n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */

//refactor code 
export function findCommonItems (firstArray, secondArray){

  const firstSet = new Set(firstArray);
  const secondSet = new Set(secondArray);

  const commonSet = firstSet.intersection(secondSet);
  

  return [...commonSet];
}


// This refactor code is better because it avoid to check every single item from two arrays for filter items & searching that each items includes in the second array . 
