# Dictionary to store the answers 
cache = {}

def fibonacci(n):
    # If we already know the answer, just use it
    if n in cache:
        return cache[n]

    # The first two numbers in Fibonacci are 0 and 1
    if n <= 1:
        result = n
    else:
        # Else find the result by adding the two previous numbers
        result = fibonacci(n - 1) + fibonacci(n - 2)

    # Remember this result so we don’t calculate it again later
    cache[n] = result
    return result
