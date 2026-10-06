/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:O(n2)
 * Space Complexity:O(1)
 * Optimal Time Complexity:O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */

/*
export function hasPairWithSum(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return true;
      }
    }
  }
  return false;
}
  */

//refactor code 

export function hasPairWithSum(numbers,target){
  const seen = new Set();

  for (const num of numbers)
  {
    const needed = target-num;
    if (seen.has(needed))
    {
      return true;
    }
    else
    {
      seen.add(num);
    }
  }

}


// The refactor code is better because it avoid nested loop but it create set so space complexity will be o(n).