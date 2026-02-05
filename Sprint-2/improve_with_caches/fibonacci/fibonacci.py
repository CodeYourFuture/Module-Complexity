_fib_cache = {}

def fibonacci(n):
    if n in _fib_cache:
        return _fib_cache[n]
    
    if n <= 1:
        x = n
    else:
        x = fibonacci(n - 1) + fibonacci(n - 2)
    _fib_cache[n] = x
    return x