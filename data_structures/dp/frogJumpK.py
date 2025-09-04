def frogJumpK(n, heights, k): 
    dp = [-1] * (n + 1) 
    dp[0] = 0 
    for i in range(1, len(dp)): 
        minJump = float('inf') 
        for j in range(1, k + 1): 
            if (i - j) >= 0: 
                jumpK = dp[i - j] + (abs(heights[i - j] - heights[i])) 
                minJump = min(jumpK, minJump) 

        dp[i] = minJump 
    return dp[n] 

height = [30,10,60,10,60,50] 
n = 5 
k = 2 
l = frogJumpK(5, height, 2) 
print("Frog jump: ", l) 


