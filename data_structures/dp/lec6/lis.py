def lis(ind, arr, prev_index): 
    if (ind == len(arr)): 
        return 0
    notTaken = 0 + lis(ind + 1, arr, prev_index) 
    taken = 0 
    if (arr[ind] > arr[prev_index] or prev_index == -1 ): 
        taken = 1 + lis(ind + 1, arr, ind) 
    return max(taken, notTaken) 


def lisMem(ind, prev_index, arr, dp): 
    if ind == len(arr): 
        return 0 
    
    if dp[ind][prev_index + 1] != -1: 
        return dp[ind][prev_index + 1] 
    
    taken = 0 
    notTaken = 0 + lisMem(ind + 1, prev_index, arr, dp) 
    if (arr[ind] > arr[prev_index] or prev_index == -1): 
        taken = 1 + lisMem(ind + 1, ind, arr, dp) 

    dp[ind][prev_index + 1] = max(taken, notTaken) 
    return dp[ind][prev_index + 1]


def lisMemStart(arr): 
    dp = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr))] 
    return lisMem(0, -1, arr, dp)


prices = [7,6,2,8] 
print(lisMemStart(prices)) 