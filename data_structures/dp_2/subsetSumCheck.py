def subsetSumCheck(index, target, arr): 
    if target == 0: 
        return True 
    
    if index == len(arr): 
        return False 
    
    taken = False 
    notTaken = subsetSumCheck(index + 1, target, arr) 

    if arr[index] <= target: 
        taken = subsetSumCheck(index + 1, target - arr[index], arr) 

    return taken or notTaken 


def mainSubsetSum(target, arr): 
    return subsetSumCheck(0, target, arr) 

def tabulatedSolution(target, arr): 
    dp = [[False for _ in range(target + 1)] for _ in range(len(arr))]

    for k in range(len(arr)): 
        dp[k][0] = True 

    if arr[0] <= target: 
        dp[0][arr[0]] = True

    for i in range(1, len(arr)): 
        for j in range(1, target + 1):  
            taken = False 
            if arr[i] <= j:
                taken = dp[i - 1][j - arr[i]] 

            notTaken = dp[i - 1][j] 
            dp[i][j] = taken or notTaken

    return dp[len(arr) - 1][target] 

def partitionSubsetSum(arr):
    totalSum = sum(arr) 
    if totalSum % 2 == 1: 
        return False 
    else: 
        return tabulatedSolution(totalSum // 2, arr) 
    

def recursiveCountSubsetsWithSumK(index, arr, target): 
    if target == 0:
        return 1 
    
    if index == 0: 
        if target == arr[index]: 
            return 1 
        else: 
            return 0 
        
    take = 0 
    if arr[index] <= target: 
        take = recursiveCountSubsetsWithSumK(index - 1, arr, target - arr[index]) 
    notTaken = recursiveCountSubsetsWithSumK(index - 1, arr, target) 

    return take + notTaken


def countSubsetsWithSumK(arr, target):
    pass

newArr = [1,2,3,4] 
target = 15 


print(tabulatedSolution(target, newArr))