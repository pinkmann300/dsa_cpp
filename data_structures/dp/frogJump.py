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


height = [30, 10, 60, 10, 60, 50]
n = 5

print(frogJumpTab(n, height))
