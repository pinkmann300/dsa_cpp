def bsFee(arr, ind, buy, fee): 
    if ind == len(arr): 
        return 0 
    
    if buy == 0:
        op1 = -arr[ind] + bsFee(arr, ind + 1, 1, fee) 
        op2 = 0 + bsFee(arr, ind + 1, 0, fee) 

    if buy == 1: 
        op1 = arr[ind] - fee + bsFee(arr, ind + 1, 0, fee) 
        op2 = 0 + bsFee(arr, ind + 1, 1, fee) 

    return max(op1, op2) 

def bsFee2(arr, ind, buy, fee, dp): 
    if (ind == len(arr)): 
        return 0 
    
    if dp[ind][buy] != -1: 
        return dp[ind][buy] 
    
    if buy == 0: 
        op1 = -arr[ind] + bsFee2(arr, ind + 1, 1, fee, dp) 
        op2 = 0 + bsFee2(arr, ind + 1, 0, fee, dp) 

    if buy == 1: 
        op1 = arr[ind] - fee + bsFee2(arr, ind + 1, 0, fee, dp)
        op2 = 0 + bsFee2(arr, ind + 1, 1, fee, dp) 

    dp[ind][buy] = max(op1, op2) 

    return dp[ind][buy] 

def bsMemo(arr, fee): 
    dp = [[-1 for _ in range(2)] for _ in range(len(arr))]
    return (bsFee2(arr, 0, 0, fee, dp)) 




prices = [1, 3, 2, 8, 4, 9]
n = len(prices)
fee = 2
result = bsMemo(prices,fee) 
print(f"The maximum profit that can be generated is {result}")
