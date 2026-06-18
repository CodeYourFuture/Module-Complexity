def fibonacci(n, cache=None):
    if cache == None:
        cache={0:0, 1:1}
    if n in cache:
        return cache[n]
    else:
        value = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        cache[n] = value
        return value
