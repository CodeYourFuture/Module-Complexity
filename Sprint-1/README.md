# Sprint 1

### Learning Objectives:

<!--{{<objectives>}}>-->

- [ ] Identify areas of inefficiency that contribute to higher time or space complexity
- [ ] Refactor the code to reduce its complexity.
<!--{{</objectives>}}>-->

There are some common programming tasks in this folder. The same tasks are provided in both JavaScript and Python. You should solve each task in one language. We recommend you pick some tasks in each language.

### For each task you undertake:

1. Identify the section(s) of code that contribute to the complexity of the code.
1. Explain the complexity using Big O notation.
1. Identify whether the complexity can be reduced. If so, refactor the code to reduce its complexity. If you don't think the complexity can be reduced, explain why not in a comment.
1. Provide the refactored code and briefly set out the complexity of your refactor.

## Next, open at least one PR

1. Open a PR with your changes, explaining what you have done and why. Include any resources you used to complete your work.
1. Now go and find another PR from a colleague.
1. **Review** this PR. Do you agree with their analysis? What about their solution or solutions? Is there a more efficient strategy you could share with your colleague to improve the code. If so, how can you show clearly and respectfully that your strategy is more efficient?

You can review as many PRs as you like. You must respond to the reviews you receive. You can use class time to complete this project.

## Running Tests

### Python Tests

First, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
# Run all tests once
pytest -v

# Run all tests in watch mode (auto-rerun on file changes)
pytest -v --watch
```

### JavaScript Tests

Navigate to the JavaScript directory first.

```bash
# Run all tests once
npm run test

# Run all tests in watch mode (auto-rerun on file changes)
npm run test:watch
```

## Resources

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted
- https://www.w3schools.com/python/ref_set_intersection.asp
- https://www.w3schools.com/python/ref_func_sorted.asp
- https://www.hellointerview.com/learn/code/two-pointers/overview
- https://www.youtube.com/watch?v=syTs9_w-pwA

###

> [!TIP]
> Big-O notation focuses on the _dominant trend_ of how resource usage grows as the input size n gets very large. It simplifies things by ignoring constant factors (multipliers) and lower-order terms.
>
> For example, an algorithm that takes `2n` steps and another that takes `n` steps are both considered O(n) (Linear Time). Why? Because as `n` gets huge, both grow directly in proportion to n. The factor of 2 doesn't change the fundamental linear growth pattern.
>
> Similarly, if you have two separate loops, each running `n` times (total `2n` steps), the complexity is still `O(n)`. This is different from nested loops, where one loop runs n times inside another loop that also runs n times, leading to `n * n` or `O(n²)` complexity.
