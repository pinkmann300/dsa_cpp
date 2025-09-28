def bsCapRec(arr, ind, cap, buy): 
    if (ind == len(arr) or cap == 0): 
        return 0 
    
    if buy == 0:
        op1 = -arr[ind] + bsCapRec(arr, ind + 1, cap, 1) 
        op2 = 0 + bsCapRec(arr, ind + 1, cap, 0)

    if buy == 1: 
        op1 = arr[ind] + bsCapRec(arr, ind + 1, cap - 1, 0) 
        op2 = bsCapRec(arr, ind + 1, cap, 1) 

    return max(op1, op2) 


def bsCapRecMemo(arr, ind, cap, buy, dp): 
    if (ind == len(arr) or cap == 0): 
        return 0 
    
    if dp[ind][buy][cap] != -1: 
        return dp[ind][buy][cap] 
    
    if buy == 0: 
        op1 = -arr[ind] + bsCapRecMemo(arr, ind + 1, cap, 1, dp) 
        op2 = 0 + bsCapRecMemo(arr, ind + 1, cap, 0, dp) 

    if buy == 1: 
        op1 = arr[ind] + bsCapRecMemo(arr, ind + 1, cap - 1, 0, dp) 
        op2 = 0 + bsCapRecMemo(arr, ind + 1, cap, 1, dp) 

    dp[ind][buy][cap] = max(op1, op2)   
    return dp[ind][buy][cap] 


def bsCapMemStart(arr): 
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(arr))] 
    return bsCapRecMemo(arr, 0, 2, 0, dp) 


def bsCapTabulate(arr): 
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(arr) + 1)] 
    for i in range(len(arr) - 1, -1, -1): 
        for j in range(2): 
            for k in range(1,3): 
                if j == 0: 
                    op1 = -arr[i] + dp[i + 1][1][k] 
                    op2 = dp[i + 1][0][k] 

                if j == 1: 
                    op1 = arr[i] + dp[i + 1][0][k - 1] 
                    op2 = dp[i + 1][1][k] 

                dp[i][j][k] = max(op1, op2) 
    return dp[0][0][2] 


 

prices = [3, 3, 5, 0, 0, 3, 1, 4]
max_profit = bsCapTabulate(prices)  
print(max_profit)
