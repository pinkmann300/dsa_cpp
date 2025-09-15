def unboundedKnapSackRec(weight, wts, val, index): 
    if index == 0: 
        if (wts >= weight[0]): 
            return ((wts // weight[0]) * val[0])
        else: 
            return 0  
    taken = 0 
    if (weight[index] <= wts): 
        taken = val[index] + unboundedKnapSackRec(weight, wts - weight[index], val, index) 
    notTaken = 0 + unboundedKnapSackRec(weight, wts, val, index - 1)
    return max(taken, notTaken) 

def unboundedMemo(weight, wts, val, index, dp): 
    if index == 0: 
        if (wts >= weight[0]): 
            return ((wts // weight[0]) * val[0])
        else: 
            return 0  
    if dp[index][wts] != -1: 
        return dp[index][wts] 
    taken = 0 
    if (weight[index] <= wts): 
        taken = val[index] + unboundedKnapSackRec(weight, wts - weight[index], val, index) 
    notTaken = 0 + unboundedKnapSackRec(weight, wts, val, index - 1)
    dp[index][wts] = max(taken, notTaken) 
    return dp[index][wts]

def unboundedMemS(weight, wts, val): 
    dp = [[-1 for _ in range(wts + 1)] for _ in range(len(weight))] 
    return unboundedMemo(weight, wts, val,len(weight) - 1 ,dp) 


def unboundedTabulation(weight, wts, val): 
    dp = [[0 for _ in range(wts + 1)] for _ in range(len(weight))] 
    for i in range(wts + 1): 
        dp[0][i] = (i // weight[0]) * val[0]

    for row in range(1, len(weight)): 
        for wtsVal in range(wts + 1): 
            notTaken = dp[row - 1][wtsVal] 
            taken = 0 
            if (weight[row] <= wtsVal): 
                taken = val[row] + dp[row][wtsVal - weight[row]] 
            dp[row][wtsVal] = max(taken, notTaken) 
    return dp[len(weight) - 1][wts] 

            





wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
print(unboundedTabulation(wt, W, val))



