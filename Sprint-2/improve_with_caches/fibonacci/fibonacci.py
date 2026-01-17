# Create a dictionary to use as our "Notepad" (Cache)
memo = {}

def fibonacci(n):
    # Check if we already calculated this number
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    result = fibonacci(n - 1) + fibonacci(n - 2)

    # Save the result in our Notepad before returning
    memo[n] = result
    
    return result