def bs2Rec(ind, buy, arr):
    if (ind == len(arr)): 
        return 0 
    
    if buy == 0: 
        op1 = -arr[ind] + bs2Rec(ind + 1, 1, arr) 
        op2 = 0 + bs2Rec(ind + 1, 0, arr) 

    if buy == 1: 
        op1 = arr[ind] + bs2Rec(ind + 1, 0, arr) 
        op2 = 0 + bs2Rec(ind + 1, 1, arr) 

    return max(op1, op2) 

def bs2Memo(ind, buy, arr, dp): 
    if ind == len(arr): 
        return 0
    if dp[ind][buy] != -1: 
        return dp[ind][buy] 
    if buy == 0: 
        op1 = -arr[ind] + bs2Memo(ind + 1, 1, arr, dp) 
        op2 = 0 + bs2Memo(ind + 1, 0, arr, dp) 
    if buy == 1: 
        op1 = arr[ind] + bs2Memo(ind + 1, 0, arr, dp) 
        op2 = 0 + bs2Memo(ind + 1, 1, arr, dp) 
    dp[ind][buy] = max(op1, op2) 
    return dp[ind][buy]


def bs2MemStart(arr): 
    dp = [[-1 for _ in range(2)] for _ in range(len(arr))] 
    return bs2Memo(0, 0, arr, dp) 

arr = [7, 1, 5, 3, 6, 4] 
print(bs2MemStart(arr)) 
