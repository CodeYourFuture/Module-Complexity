def fibonacci(n,fib_memo={}):
     # fib_memo is a default mutable dictionary used to cache computed Fibonacci values
    # This allows memoisation: results are stored and reused across recursive calls
    
    if n <= 1:
        return n
    if n in fib_memo:
        # Return cached value if already computed
        return fib_memo[n]
    else:
        result=fibonacci(n - 1) + fibonacci(n - 2)

        # Store computed value in cache
        fib_memo[n]=result
        
    return result
