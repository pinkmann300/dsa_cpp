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

arr = [7, 1, 5, 3, 6, 4] 
print(bs2Rec(0, 0, arr)) 
