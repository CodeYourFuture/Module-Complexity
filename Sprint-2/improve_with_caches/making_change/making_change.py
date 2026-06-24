def ways_to_make_change(total: int) -> int:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    dp = [0] * (total + 1)
    
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] += dp[i - coin]
            
    return dp[total]