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

def bsFeeTab(arr, fee): 
    dp = [[0 for _ in range(2)] for _ in range(len(arr) + 1)] 
    dp[len(arr)][0] = 0 
    dp[len(arr)][1] = 0 

    for i in range(len(arr) - 1, -1, -1): 
        for k in range(2): 
            if (k == 0): 
                op1 = -arr[i] + dp[i + 1][1] 
                op2 = dp[i + 1][0] 
            if (k == 1): 
                op1 = arr[i] - fee + dp[i + 1][0] 
                op2 = dp[i + 1][1] 
            
            dp[i][k] = max(op1, op2) 

    return dp[0][0]


prices = [1, 3, 2, 8, 4, 9]
n = len(prices)
fee = 2
result = bsFeeTab(prices,fee) 
print(f"The maximum profit that can be generated is {result}")
