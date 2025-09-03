def frogJumpTab(n, heights):
    dp = [-1] * (n + 1) 

    dp[0] = 0 

    for i in range(1, len(dp)): 
        jumpTwo = float('inf')
        jumpOne = dp[i - 1] + (abs(heights[i - 1] - heights[i])) 

        if (i > 1): 
            jumpTwo = dp[i - 2] + (abs(heights[i - 2] - heights[i])) 
        
        minJump = min(jumpOne, jumpTwo)
        dp[i] = minJump 
    
    return dp[n] 


def frogJumpMemoization(n, heights, dp):
    if n == 0: 
        return 0 
    if n == 1: 
        return (abs(heights[0] - heights[1])) 
    if dp[n] != -1: 
        return dp[n] 
    else: 
        jumpOne = frogJumpMemoization(n - 1, heights, dp) + (abs(heights[n - 1] -heights[n])) 
        jumpTwo = frogJumpMemoization(n - 2, heights, dp) + (abs(heights[n - 2] - heights[n])) 
        dp[n] = min(jumpOne, jumpTwo) 
        return dp[n]

height = [30, 10, 60, 10, 60, 50]
n = 5

dp = [-1] * 6
print(frogJumpMemoization(5, height, dp))