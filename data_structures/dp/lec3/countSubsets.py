def countSubsets(arr, index, target): 
    if (target == 0): 
        return 1 
    if (index == 0 and arr[0] == target): 
        return 1 
    if (index < 0): 
        return 0
    taken = 0 
    if arr[index] <= target: 
        taken = countSubsets(arr, index - 1, target - arr[index]) 
    notTaken = countSubsets(arr, index - 1, target) 
    return taken + notTaken 


def countMemoizer(arr, index, target, dp): 
    if (target == 0): 
        dp[index][target] = 1 
        return dp[index][target]
    if (index == 0 and arr[0] == target): 
        dp[index][target] = 1
        return dp[index][target]
    if (index < 0): 
        return 0
    if dp[index][target] != -1: 
        return dp[index][target] 
    taken = 0 
    if (arr[index] <= target): 
        taken = countSubsets(arr, index - 1, target - arr[index])
    notTaken = countSubsets(arr, index - 1, target) 
    dp[index][target] = taken + notTaken
    return dp[index][target] 


def countMemStarter(arr, target):
    dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr))] 
    countMemoizer(arr, len(arr) - 1, target, dp)
    print(dp)
    return dp[len(arr) - 1][target] 


def countSubsets(arr, target): 
    dpArr = [[0 for _ in range(target + 1)] for _ in range(len(arr))] 
    for index in range(len(arr)): 
        dpArr[index][0] = 1 
    if arr[0] <= target: 
        dpArr[0][arr[0]] = 1
    for i in range(1, len(arr)): 
        for j in range(1, target + 1): 
            notTaken = dpArr[i - 1][j] 
            taken = 0 
            if (arr[i] <= j): 
                taken = dpArr[i - 1][j - arr[i]] 
            dpArr[i][j] = taken + notTaken
    return dpArr[len(arr) - 1][target]

arr = [1,2,2,3] 
print(countSubsets(arr, 3)) 