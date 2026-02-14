/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:before refactoring O(n²)- after refactoring O(n log n)
 * Space Complexity:before refactoring O(1)- after refactoring O(1)
 * Optimal Time Complexity:O(n log n)
 * https://www.hellointerview.com/learn/code/two-pointers/overview
 * The refactored solution first sorts the array, which takes O(n log n) time,
 * and then uses the two-pointer technique to scan the array in a single pass (O(n)). The sorting step dominates the overall complexity.
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  numbers.sort((a,b)=>a-b);
  let left=0;
  let right=numbers.length-1;
  while (left<right) {
    const current_sum=numbers[left]+numbers[right];
    if (current_sum === target){
      return true;}
    if (current_sum<target){
      left +=1;
    } else {
      right -=1;
    }  
  }
  return false;

}
