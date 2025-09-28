def bsCoolDown(ind, arr, buy): 
    if (ind >= len(arr)): 
        return 0 
    
    if buy == 0: 
        op1 = -arr[ind] + bsCoolDown(ind + 1, arr, 1) 
        op2 = bsCoolDown(ind + 1, arr, 0) 

    if buy == 1: 
        op1 = arr[ind] + bsCoolDown(ind + 2, arr, 0) 
        op2 = bsCoolDown(ind + 1, arr, 1)

    return max(op1, op2) 

def bscMemo(ind, arr, buy, dp): 
    if (ind >= len(arr)): 
        return 0 
    
    if (dp[ind][buy] != -1): 
        return dp[ind][buy]
    
    if buy == 0:
        op1 = -arr[ind] + bscMemo(ind + 1, arr, 1, dp )
        op2 = bscMemo(ind + 1, arr, 0, dp)

    if buy == 1: 
        op1 = arr[ind] + bscMemo(ind + 2, arr, 0, dp) 
        op2 = bscMemo(ind + 1, arr, 1, dp) 

    dp[ind][buy] = max(op1, op2) 
    return dp[ind][buy] 

    
def bscMem(arr):
    dp = [[-1 for _ in range(2)] for _ in range(len(arr))] 
    return bscMemo(0, arr, 0, dp) 


prices = [4, 9, 0, 4, 10]
print(bscMem(prices)) 