def subsetSumEqTok(ind, target, arr): 
    if (target == 0): 
        return True 
    if (ind < 0): 
        return False 
    else: 
        pickedCase = False 
        if (arr[ind] <= target): 
            pickedCase = subsetSumEqTok(ind - 1, target - arr[ind], arr) 
        unPickedCase = subsetSumEqTok(ind - 1, target, arr)  

        return (pickedCase or unPickedCase) 
    
def subsetSumEqtoKMem(ind, target, arr, dp): 
    if (target == 0): 
        return True 
    if (ind < 0): 
        return False
    if (dp[ind][target] != -1): 
        return 
    else: 
        pickedCase = False 
        if (arr[ind] <= target): 
            pickedCase = subsetSumEqtoKMem(ind - 1, target - arr[ind], arr, dp) 
        unPickedCase = subsetSumEqtoKMem(ind - 1, target, arr, dp)
        dp[ind][target] = pickedCase or unPickedCase 
        return dp[ind][target]

def subMemo(target, arr):
    dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr))] 
    k = subsetSumEqtoKMem(len(arr)-1, target, arr, dp)
    return k 

def subSumTab(target, arr): 
    dp = [[False for _ in range(target + 1)] for _ in range(len(arr))]
    for k in range(len(arr)): 
        dp[k][0] = True 
    for row in range(len(arr)): 
        for col in range(1, target): 
            pass 






arr = [3,6,5]
k = subMemo(8, arr) 
print(k)