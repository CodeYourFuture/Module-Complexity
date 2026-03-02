Each directory contains implementations that can be made faster by using pre-computing.

The problem they solve is described in docstrings and tests.

Speed up the solutions by introducing precomputing. You may rewrite as much of the solution as you want, and may add any tests, but must not modify existing tests.

## Improvements Made

### common_prefix

**Original Approach (Nested Loops):**
- Time Complexity: **O(n² × m)** - Compares every string with every other string (n²) pairs, each taking O(m) comparisons

**Optimized Approach (Sort + Adjacent Pairs):**
- Time Complexity: **O(n log n + n × m)** - Sort once (n log n), then compare only adjacent pairs (n comparisons)
- **Why better:** The longest common prefix will be found in the first and last strings after sorting, eliminating unnecessary comparisons. Reduces from O(n²) to O(n) pair comparisons.

### count_letters

**Original Approach (Repeated String Checks):**
- Time Complexity: **O(n²)** - For each letter, checking if lowercase version exists in string is O(n), done n times

**Optimized Approach (Precomputed Set):**
- Time Complexity: **O(n)** - Precompute lowercase letters into a set (O(n)), then check membership is O(1) each time
- **Why better:** Replaces repeated O(n) string searches with single O(n) precomputation and O(1) set lookups, reducing overall from O(n²) to O(n).
