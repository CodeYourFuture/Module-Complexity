def fibonacci(n, cache={}):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result