def fibonacci(n):
    cache = {} 
    
    if n <= 1:
        cache[n] = n
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)
