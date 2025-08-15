def fibonacci(n, memo=None):
    if n <= 1:
        return n
    
    if memo is None:
        memo = {}
    
    if n in memo: return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

