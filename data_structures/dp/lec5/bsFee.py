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


prices = [1, 3, 2, 8, 4, 9]
n = len(prices)
fee = 2

result = bsFee(prices, 0, 0, fee) 
print(f"The maximum profit that can be generated is {result}")
