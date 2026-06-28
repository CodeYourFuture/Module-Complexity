def fibonacci(n, cache = {}):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        return cache[n]
