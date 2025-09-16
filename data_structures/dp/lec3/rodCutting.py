def rodCutting(arr): 
    return rodCuttingMemStart(arr)

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

arr = [2,5,7,8,10] 
k = rodCutting(arr) 
print(k)