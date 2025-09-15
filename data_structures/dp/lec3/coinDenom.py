def coinDenom(arr, target): 
    return coinDenomTab(arr, target) 

def coinDenomRec(arr, target, index): 
    if (target == 0): 
        return 0 
    if index == 0 :
        if (target % arr[index] == 0):
            return target // arr[index] 
        else: 
            return int(1e9) 
    taken = int(1e9) 
    if (arr[index] <= target): 
        taken = 1 + coinDenomRec(arr, target - arr[index], index) 
    notTaken = coinDenomRec(arr, target, index - 1) 
    return min(taken, notTaken) 


def coinDenomMem(arr, target, index, dp):
    if (target == 0): 
        return 0 
    if index == 0 :
        if (target % arr[index] == 0):
            return target // arr[index] 
        else: 
            return int(1e9) 
    if dp[index][target] != -1: 
        return dp[index][target] 
    taken = int(1e9) 
    if (arr[index] <= target): 
        taken = 1 + coinDenomRec(arr, target - arr[index], index) 
    notTaken = 0 + coinDenomRec(arr, target, index - 1) 
    dp[index][target] = min(taken, notTaken) 
    return dp[index][target] 

def coinDenomMemStart(arr, target): 
    dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr))] 
    return coinDenomMem(arr, target, len(arr) - 1, dp) 

def coinDenomTab(arr, target): 
    dp = [[0 for _ in range(target + 1)] for _ in range(len(arr))] 
    for i in range(target + 1): 
        if i % arr[0] == 0: 
            dp[0][i] = i // arr[0] 
        else:
            dp[0][i] = int(1e9) 

    for row in range(1,len(arr)): 
        for targetVal in range(target + 1):

            notTaken = dp[row - 1][targetVal] 
            taken = int(1e9) 
            if (arr[row] <= targetVal): 
                taken = 1 + dp[row][targetVal - arr[row]] 
            dp[row][targetVal] = min(taken, notTaken) 

    return dp[len(arr) - 1][target] 

    
arr = [1,2,3] 
target = 7 
print(coinDenom(arr, target))