cache = {} 

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        cache[n] = n
        return n
    
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result
