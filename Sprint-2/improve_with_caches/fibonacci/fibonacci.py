cache = {} 

def fibonacci(n):
    
    if n <= 1:
        cache[n] = n
        return cache
    
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return cache
