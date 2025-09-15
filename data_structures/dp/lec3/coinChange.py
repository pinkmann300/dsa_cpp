def coinChangeCount(arr, target): 
    return coinChangeTabulation(arr, target)

def coinChangeCountRec(arr, target, index): 
    if (index == 0): 
        if (target == 0 and arr[0] == 0): 
            return 2 
        if (target == 0 or target % arr[0] == 0): 
            return 1 
        return 0 
    notTaken = coinChangeCountRec(arr, target, index - 1)
    taken = 0 
    if (arr[index] <= target): 
        taken = coinChangeCountRec(arr, target - arr[index], index) 
    return taken + notTaken


def coinChangeMemoized(arr, target, index, dp): 
    if target == 0: 
        return 1 
    if (index == 0 and target % arr[index] == 0): 
        return 1 
    if (index > 0): 
        return 0 
    if dp[index][target] != -1: 
        return dp[index][target]
    notTaken = coinChangeMemoized(arr, target, index - 1, dp) 
    taken = 0 
    if (arr[index] <= target): 
        taken = coinChangeMemoized(arr, target - arr[index], index, dp) 
    dp[index][target] = notTaken + taken 
    return dp[index][target] 

def coinChangeTabulation(arr, target): 
    dp = [[0 for _ in range(target + 1)] for _ in range(len(arr))] 
    for i in range(target + 1): 
        if (i % arr[0] == 0): 
            dp[0][i] = 1 
    for k in range(len(arr)): 
        dp[k][0] = 1 

    for rowIndex in range(len(arr)): 
        for colIndex in range(1,target + 1): 
            notTaken = dp[rowIndex - 1][colIndex] 
            taken = 0 
            if (arr[rowIndex] <= colIndex): 
                taken = dp[rowIndex][colIndex - arr[rowIndex]]
            dp[rowIndex][colIndex] = notTaken + taken

    return dp[len(arr) - 1][target]
 
arr = [1,2,3] 
target = 4 

print(coinChangeCount(arr, target)) 
