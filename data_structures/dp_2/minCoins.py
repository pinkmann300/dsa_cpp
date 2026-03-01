def recusiveMinCoins(arr, index, target): 
    if index == 0: 
        if target % arr[index] == 0: 
            return (target // arr[index])
        else: 
            return float('inf') 
        
    take = float('inf') 
    notTake = 0 + recusiveMinCoins(arr, index - 1, target) 
    if arr[index] <= target: 
        take = 1 + recusiveMinCoins(arr, index, target - arr[index]) 
    
    return min(take, notTake) 

def minCoinsTabulated(arr, target): 
    dp = [[float('inf') for _ in range(target + 1)] for _ in range(len(arr))] 

    for i in range(target + 1):
        if i % arr[0] == 0: 
            dp[0][i] = i // arr[0]

    for row in range(1, len(arr)): 
        for col in range(target + 1): 
            taken = float('inf')
            notTaken = 0 + dp[row - 1][col] 
            if arr[row] <= col: 
                taken = 1 + dp[row][col - arr[row]] 
            dp[row][col] = min(taken, notTaken) 
    
    return dp[len(arr) - 1][target]

def numberOfWaysToCoin(index, target, arr): 
    if index == 0:
        if target % arr[index] == 0: 
            return 1
        else: 
            return 0 
        
    take = 0 
    notTake = numberOfWaysToCoin(index - 1, target, arr) 
    if arr[index] <= target: 
        take = numberOfWaysToCoin(index, target - arr[index], arr)

    return notTake + take 

def numberOfWaysToCoinTab(arr, target): 
    dp = [[0 for _ in range(target + 1)] for _ in range(len(arr))] 
    
    for i in range(target + 1): 
        if i % arr[0] == 0: 
            dp[0][i] = 1 
    
    for i in range(1, len(arr)): 
        for targ in range(target + 1): 
            taken = 0 
            notTaken = dp[i - 1][targ] 
            if arr[i] <= targ: 
                taken = dp[i][targ - arr[i]] 

            dp[i][targ] = taken + notTaken

    return dp[len(arr) - 1][target] 