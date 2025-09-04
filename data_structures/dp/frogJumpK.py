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

def frogJumpMemo(n, heights, k, dp): 
    if n == 0:
        return 0 
    if dp[n] != -1: 
        return dp[n] 
    else: 
        minJump = float('inf') 
        for i in range(1, k + 1):
            if (n - i) >= 0: 
                jumps = frogJumpMemo(n - i, heights, k, dp) + abs(heights[n - i] - heights[n])
                minJump = min(minJump, jumps) 
        dp[n] = minJump
        return dp[n] 


height = [30,10,60,10,60,50] 
n = 5 
k = 2 

dp = [-1] * 6
l = frogJumpMemo(5, height, 2, dp) 
print("Frog jump: ", l) 


