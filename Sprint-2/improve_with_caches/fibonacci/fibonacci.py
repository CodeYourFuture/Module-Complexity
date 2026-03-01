cache={}

def fibonacci(n): 
    '''Adding a dictionary to store a copy of what we have already calculated, the complexity becomes linear.
    With the cache, each value is computed once, bringing it down to O(n)
    '''
    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]
