/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
    // We went through the list two times, first to add the numbers, then to multiply them.
    // But we can do both in one loop. This makes the code a bit simpler and faster.
    
    // let sum = 0;
    // for (const num of numbers) {
    //     sum += num;
    // }

    // let product = 1;
    // for (const num of numbers) {
    //     product *= num;
    // }

    // return {
    //     sum: sum,
    //     product: product,
    // };

    // My solution

    let sum = 0;
    let product = 1;
    for (const num of numbers) {
        sum += num;
        product *= num;
    }

    return {
        sum: sum,
        product: product,
    };
}


