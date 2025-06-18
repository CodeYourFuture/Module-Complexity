/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(m + n) — build set and loop through arrays once
 * Space Complexity: O(n) — store second array in a set
 * Optimal Time Complexity: O(m + n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
// export const findCommonItems = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
// ];

// My solution. Refactored to use a Set for faster lookups, making the code more efficient
 
export const findCommonItems = (firstArray, secondArray) => {
    // Turn secondArray into a Set to quickly check if items exist
    const secondSet = new Set(secondArray);
    // Create a Set to keep track of common items without duplicates
    const commonItemsSet = new Set();

    // Go through each item in firstArray
    for (const element of firstArray) {
        // If the item is found in secondSet, add it to commonItemsSet
        if (secondSet.has(element)) {
            commonItemsSet.add(element);
        }
    }
    // Change the Set of common items back into an array to return
    return [...commonItemsSet];
};
