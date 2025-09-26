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


prices = [4, 9, 0, 4, 10]
print(bsCoolDown(0, prices, 0)) 