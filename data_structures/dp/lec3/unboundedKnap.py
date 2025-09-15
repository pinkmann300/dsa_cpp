def unboundedKnapSackRec(weight, wts, val, index): 
    if index == 0: 
        if (wts >= weight[index]): 
            return ((wts // weight[index]) * val[index])
        else: 
            return 0  
    taken = 0 
    if (weight[index] <= wts): 
        taken = val[index] + unboundedKnapSackRec(weight, wts - weight[index], val, index) 
    notTaken = 0 + unboundedKnapSackRec(weight, wts, val, index - 1)
    return max(taken, notTaken) 

wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
print(unboundedKnapSackRec(wt, W, val, 2))



