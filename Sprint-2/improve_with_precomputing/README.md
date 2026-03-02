Each directory contains implementations that can be made faster by using pre-computing.

The problem they solve is described in docstrings and tests.

Speed up the solutions by introducing precomputing. You may rewrite as much of the solution as you want, and may add any tests, but must not modify existing tests.

## Improvements Made

### common_prefix

**Problem:** Find the longest common prefix among any two strings in a list.

**Original Approach (Nested Loops):**
- **Time Complexity:** O(n² × m)
  - Compares every string with every other string: O(n²) pairs
  - Each string comparison takes O(m), where m is the average string length
  - Total: n² string comparisons, each O(m)

**Optimized Approach (Sort + Adjacent Pairs):**
- **Time Complexity:** O(nm log n)
  - Sorting n strings: O(nm log n) where each comparison is O(m)
  - Comparing adjacent pairs: O(nm) for n-1 comparisons
  - Dominated by sorting: O(nm log n)

**Why Better:** After sorting, strings with common prefixes become adjacent. We only need to compare n-1 adjacent pairs instead of all n² possible pairs. This reduces the number of pair comparisons from O(n²) to O(n), making it significantly faster for large inputs.

---

### count_letters

**Problem:** Count letters that only occur in uppercase in a string.

**Original Approach (Repeated String Searches):**
- **Time Complexity:** O(n²)
  - For each character: check if `letter.lower() in s` → O(n) search
  - Repeated for n characters → O(n²) total

**Optimized Approach (Precomputed Set):**
- **Time Complexity:** O(n)
  - Build set of lowercase letters: O(n)
  - Check each uppercase letter against set: O(1) per lookup
  - Total: O(n) + O(n) = O(n)

**Why Better:** By precomputing all lowercase letters into a set once (O(n)), we replace n repeated O(n) string searches with O(1) set lookups. This reduces the overall complexity from O(n²) to O(n).

Why better: Replaces repeated O(n) string searches with single O(n) precomputation and O(1) set lookups, reducing overall complexity from O(n²) to O(n).

**Original Approach (Repeated String Checks):**
- Time Complexity: **O(n²)** - For each letter, checking if lowercase version exists in string is O(n), done n times

**Optimized Approach (Precomputed Set):**
- Time Complexity: **O(n)** - Precompute lowercase letters into a set (O(n)), then check membership is O(1) each time
- **Why better:** Replaces repeated O(n) string searches with single O(n) precomputation and O(1) set lookups, reducing overall from O(n²) to O(n).
