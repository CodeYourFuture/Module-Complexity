_memo = {}

def fibonacci(n):
    if n in _memo:
        return _memo[n]
    if n <= 1:
        return n
    
    _memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return _memo[n]
