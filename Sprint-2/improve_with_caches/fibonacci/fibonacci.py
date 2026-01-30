memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result

    return result
