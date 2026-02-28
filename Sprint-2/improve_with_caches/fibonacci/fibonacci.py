fibonacci_cache = {}

def fibonacci(n):
    if(n) in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 1:
        return n
    
    result = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = result 
    return result
