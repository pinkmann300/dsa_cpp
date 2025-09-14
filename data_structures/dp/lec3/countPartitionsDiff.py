def countSubsets(arr, index, target): 
    if (index == 0): 
        if (target == 0 and arr[0] == 0): 
            return 2 
        if (target == 0 or arr[0] == target): 
            return 1 
        return 0 
    else: 
        taken = 0 
        notTaken = countSubsets(arr, index - 1, target) 
        if (arr[index] <= target): 
            taken = countSubsets(arr, index - 1, target - arr[index]) 
        return notTaken + taken 
    
def countSubsetsMemoStart(arr, target): 
    n = len(arr) - 1 
    dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)] 
    return countSubsetsMemoized(arr, n, target, dp) 

def countSubsetsMemoized(arr, index, target, dp): 
    if (index == 0): 
        if (target == 0 and arr[0] == 0): 
            return 2 
        if (target == 0 or arr[0] == target): 
            return 1 
        return 0 
    if (dp[index][target] != -1): 
        return dp[index][target] 
    taken = 0 
    notTaken = countSubsetsMemoized(arr, index - 1, target, dp)
    if (arr[index] <= target): 
        taken = countSubsetsMemoized(arr, index - 1, target - arr[index]) 
    dp[index][target] = taken + notTaken 
    return dp[index][target] 

def countSubsetsTabulation(arr, target): 
    dp = [[0 for _ in range(target + 1)] for _ in range(len(arr))] 
    for i in range(len(arr)): 
        dp[i][0] = 1 
    if (arr[0] == 0): 
        dp[0][0] = 2 
    if (arr[0] <= target): 
        dp[0][arr[0]] = 1 
    for rowIndex in range(1,len(arr)): 
        for targetIndex in range(1, target + 1): 
            taken = 0 
            notTaken = dp[rowIndex - 1][targetIndex] 
            if (arr[rowIndex] <= targetIndex): 
                taken = dp[rowIndex - 1][targetIndex - arr[rowIndex]] 

            final = taken + notTaken 
            dp[rowIndex][targetIndex] = final 
    return dp[len(arr) - 1][target] 

def countSubsetsGivenDiff(arr, difference): 
    totalSum = sum(arr) 
    s1_sum = totalSum - difference
    if (s1_sum % 2 == 1):
        return 0 
    else: 
        return countSubsetsTabulation(arr, s1_sum // 2) 

arr = [5,2,6,4]
k = 3
print(countSubsetsGivenDiff(arr, 3)) 