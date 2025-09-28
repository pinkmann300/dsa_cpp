def lis(ind, arr, prev_index): 
    if (ind == len(arr)): 
        return 0
    
    notTaken = 0 + lis(ind + 1, arr, prev_index) 
    taken = 0 

    if (arr[ind] > arr[prev_index] or prev_index == -1 ): 
        taken = 1 + lis(ind + 1, arr, ind) 

    return max(taken, notTaken) 


prices = [7,6,2,8] 
print(lis(0,prices, -1)) 



