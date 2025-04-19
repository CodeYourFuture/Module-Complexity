import {calculateSumAndProduct} from "./calculateSumAndProduct.js";
import assert from "node:assert/strict";

console.log("Testing calculateSumAndProduct...");

// Test normal case
assert.deepStrictEqual(
  calculateSumAndProduct([1, 2, 3, 4]),
  {sum: 10, product: 24},
  "Should calculate sum and product correctly"
);

// Test with negative numbers
assert.deepStrictEqual(
  calculateSumAndProduct([-1, 2, -3, 4]),
  {sum: 2, product: 24},
  "Should handle negative numbers"
);

// Test with repeated numbers
assert.deepStrictEqual(
  calculateSumAndProduct([2, 2, 2]),
  {sum: 6, product: 8},
  "Should handle repeated numbers"
);

// Test edge case - empty array
assert.deepStrictEqual(
  calculateSumAndProduct([]),
  {sum: 0, product: 1},
  "Should handle empty array"
);

console.log("✓ All calculateSumAndProduct tests passed!");
