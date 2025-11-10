# Cache dictionary to store computed Fibonacci values
fib_cache = {}

def fibonacci(n):
    # Check if we already computed this value
    if n in fib_cache:
        return fib_cache[n]
    
    # Base cases
    if n <= 1:
        fib_cache[n] = n
        return n
    
    # Recursive case with caching
    result = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = result
    return result