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
// My analysis report
// The function have a hidden nested loop using filter() and includes() This makes it quite expensive for us

// Time Complexity
// .filter() does n operation and .includes() does m operation since it is a nested loop the time complexity would be the product of the two complexities
// O (n * m )
// Space Complexity
// .filter creates a temporary array to store common items O(n) space and "Set" also takes O(m) space. This is un avoidable if we use this nested loop

// The inefficiency is on the hidden nested loop

export const findCommonItems = (firstArray, secondArray) => {
  const arraySet = new Set(secondArray);
  const commonItems = firstArray.filter((item) => {
    return arraySet.has(item);
  });

  return [...new Set(commonItems)];
};


// Time complexity is O(n + m) which is O(n) complexity from line 28 and o(m) complexity from line 32. i neglected line 27 complexity since it is O(1)
// Space Complexity stays almost same
// and we can say refactoring this code makes it fast.  
