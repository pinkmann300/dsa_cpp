def memoizedApp(n, dp):
    if (n <= 1):
        return 1 

    if (dp[n] != -1): 
        return dp[n]

    else: 
        dp[n] = memoizedApp(n - 1, dp) + memoizedApp(n - 2, dp)
        return dp[n] 


if __name__ == "__main__": 
    dp1 = [-1] * 5 #Essentially find the number of ways it takes to reach the 4th step. 
    k = memoizedApp(3, dp1) 
    print(k) 


    