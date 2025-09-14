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
    
def printSubsequences(arr, genVal): 
    if (len(arr) == 0): 
        return [genVal] 
    else: 
        k = printSubsequences(arr[1:], genVal + [arr[0]]) 
        r = printSubsequences(arr[1:], genVal) 
        return k + r   
    
def iterativeSubsequences(arr): 
    results = [] 
    results.append([]) 
    for k in range(len(arr)):     
        elem = arr[k] 
        for i in range(len(results)): 
            newResult = results[i] + [elem] 
            results = results + [newResult] 
    return results 

height = [10,20,30,40,50] 
n = 5 
k = 2 
m = len(iterativeSubsequences(height)) 
print(m)


