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

newArr = [1,2,3,4] 
target = 15 


print(tabulatedSolution(target, newArr))