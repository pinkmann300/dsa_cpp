def rodCutting(arr): 
    return rodCuttingTabulation(arr)

def rodCuttingRec(arr, remLength, index): 
    if (remLength == 0): 
        return 0 
    if (index == 0): 
        return remLength * arr[0] 
    notTaken = 0 + rodCuttingRec(arr, remLength, index - 1)
    taken = 0 
    if (remLength >= (index + 1)):
        taken = arr[index] + rodCuttingRec(arr, remLength - index - 1, index) 
    return max(taken, notTaken)

def rodCuttingMemo(arr, remLength, index, dp): 
    if (remLength == 0):
        return 0 
    if (index == 0): 
        return remLength * arr[0] 
    if (index < 0): 
        return 0 
    if (dp[index][remLength] != -1): 
        return dp[index][remLength] 
    
    notTaken = 0 + rodCuttingMemo(arr, remLength, index - 1, dp) 
    taken = 0 
    if (remLength >= (index + 1) ): 
        taken = arr[index] + rodCuttingMemo(arr, remLength - index - 1, index, dp) 
    dp[index][remLength] = max(taken, notTaken) 
    return dp[index][remLength]

def rodCuttingMemStart(arr): 
    dp = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr))] 
    return rodCuttingMemo(arr, len(arr), len(arr) - 1, dp) 

def rodCuttingTabulation(arr): 
    n = len(arr)
    dp = [[0 for _ in range(n + 1)] for _ in range(n)] 
    
    # Base case: only first rod length (1) is used
    for i in range(n + 1): 
        dp[0][i] = i * arr[0] 
    for row in range(1, n): 
        for reml in range(n + 1): 
            notTaken = dp[row - 1][reml] 
            taken = 0 
            rodLength = row + 1
            if reml >= rodLength: 
                taken = dp[row][reml - rodLength] + arr[row] 
            dp[row][reml] = max(taken, notTaken) 
    print(dp)
    return dp[n - 1][n]

arr = [2,5,7,8,10] 
k = rodCutting(arr) 
print(k)