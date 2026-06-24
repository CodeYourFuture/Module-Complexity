def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative integers.")
    if n <= 1:
        return n
        
    # Track the last two numbers in the sequence
    prev2 = 0  # fibonacci(0)
    prev1 = 1  # fibonacci(1)
    
    # Calculate upward to n
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return prev1