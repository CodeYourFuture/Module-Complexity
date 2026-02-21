#initialising a dictionary to store a copy of what we already know or have already computed
#caching reduces the fibonacci time complexity from exponential to linear.
cache = {}

def fibonacci(n):
    if n in cache: 
        return cache[n]
    
    if n <= 1: #when n is 0 or 1, we don’t need to calculate anything,just return th known value
        return n
    
    result = fibonacci(n - 1) + fibonacci(n - 2)
    
    #saving result in our dict before returning 
    cache[n] = result
    return result

