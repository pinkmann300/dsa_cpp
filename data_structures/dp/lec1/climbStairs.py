def memoizedApp(n, dp):
    if (n <= 1):
        return 1 
    if (dp[n] != -1): 
        return dp[n]
    else: 
        dp[n] = memoizedApp(n - 1, dp) + memoizedApp(n - 2, dp)
        return dp[n] 
    
def tabulation(n): 
    if (n <= 1): 
        return 1 
    prev_2 = 1 
    prev_1 = 1 
    index = 2
    current = 0
    while (index <= n): 
        current = prev_2 + prev_1 
        prev_2 = prev_1 
        prev_1 = current 
        index += 1 
    return current

if __name__ == "__main__": 
    k = tabulation(4)
    print(k) 


    