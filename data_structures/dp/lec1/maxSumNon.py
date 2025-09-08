def maxSumNonAdj(arr): 
    n = len(arr) 
    dp = [-1] * n 
    dp[0] = arr[0] 
    for i in range(1,n): 
        pick = arr[i] 
        if i > 1: 
            pick += dp[i - 2] 
        nonPick = dp[i - 1]

        dp[i] = max(pick, nonPick) 
    return dp[n-1] 

def robberies(arr): 
    ans1 = maxSumNonAdj(arr[1:]) 
    ans2 = maxSumNonAdj(arr[0:len(arr) - 1]) 
    return max(ans1, ans2)

arr = [2,3,2] 
print(robberies(arr)) 