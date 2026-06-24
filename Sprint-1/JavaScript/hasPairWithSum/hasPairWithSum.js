/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: is O(n^2) coz we have nested loop in the function
 * Space Complexity: is O(n) coz it grows proportionally with the input size    
 * Optimal Time Complexity: to O(n) - and that by using Set as check point to fast lookup and catch up if it has the number instead of re-scanning everything
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const checkPoint = new Set()

  for(let i=0; i < numbers.length; i++){
    let num = target - numbers[i]
    if(checkPoint.has(num)){
      return true
    }else {
      checkPoint.add(numbers[i])
    }
  }
  
  return false;
}

console.log(hasPairWithSum([1, 2, 4, 5, 3], 9));
