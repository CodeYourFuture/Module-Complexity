def fibonacci(n):
    cache = {} 
    
    if n <= 1:
        cache[n] = n
        return n
    
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result
