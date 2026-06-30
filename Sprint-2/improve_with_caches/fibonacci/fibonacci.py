_cache = {}

def fibonacci(n):
    if n in _cache:
        return _cache[n]
    
    if n <= 1:
        return n
    
    result = fibonacci(n - 1) + fibonacci(n - 2)
    _cache[n] = result
    return result
