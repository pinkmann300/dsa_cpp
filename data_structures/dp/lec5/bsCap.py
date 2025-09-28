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

prices = [3, 3, 5, 0, 0, 3, 1, 4]
max_profit = bsCapRec(prices, 0, 2, 0) 
print(max_profit)
