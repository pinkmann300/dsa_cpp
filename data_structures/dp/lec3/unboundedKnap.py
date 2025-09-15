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



wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
print(unboundedMemS(wt, W, val))



