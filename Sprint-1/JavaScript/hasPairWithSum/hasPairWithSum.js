/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  // we start with an empty box called seenNumbers to remember what we look at
  // before with two loops, an array of 1,000 numbers would take 1 milion steps
  // Now, with this box, we only need to look at each number exactly one time.
  const seenNumbers = new Set();
  // This loop goes through the list of numbers just one single time
  for (const num of numbers) {
    // get the "missing partner" number we need to hit the target sum
    const complement = target - num;
    // We check our box. Is the missing partner already inside?
    // Checking this box is super fast for computers
    if (seenNumbers.has(complement)) {
      // if the partner is in the box, we found a matching pair , we sent true
      return true;
    }
    // if the partner isn't in the box yet, put the current number in the box so we remember it for later
    seenNumbers.add(num);
  }

  return false;
}


