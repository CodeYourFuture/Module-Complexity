def fibonacci(n):
    if n in fibonacci.cache:
        return fibonacci.cache[n]
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci.cache[n] = value
        return value

fibonacci.cache={0:0, 1:1}