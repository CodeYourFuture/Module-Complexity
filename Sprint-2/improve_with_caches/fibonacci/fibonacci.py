_fibonacci_cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in _fibonacci_cache:
        return _fibonacci_cache[n]
    value = fibonacci(n - 1) + fibonacci(n - 2)
    _fibonacci_cache[n] = value
    return value
