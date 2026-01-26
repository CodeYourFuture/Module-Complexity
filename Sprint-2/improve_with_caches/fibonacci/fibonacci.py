cache = {}


def fibonacci(n):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]
