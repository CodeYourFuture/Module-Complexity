fib_cache = {}
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    if n in fib_cache:
        return fib_cache[n]
    
    fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    
    return fib_cache[n]