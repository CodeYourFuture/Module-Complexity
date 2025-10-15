#def fibonacci(n):
#    if n <= 1:
#       return n 
#  return fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci(n, cache=None):   #cache dict is created only once to store results of previous calls.
    if cache is None:
        cache = {}

    if n in cache:   #if n is already cached return it
        return cache[n]

    if n <= 1:   #If not cached, n <= 1, return base case (0 or 1)
        cache[n] = n
    else:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache) #Cache the computed value for future reuse

    return cache[n].    #Return the cached or newly computed value.
