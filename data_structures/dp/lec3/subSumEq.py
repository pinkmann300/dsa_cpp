def subsetSumEqTok(ind, target, arr): 
    if (target == 0): 
        return True 
    if (ind < 0): 
        return False 
    
    else: 
        pickedCase = False 
        if (arr[ind] <= target): 
            pickedCase = subsetSumEqTok(ind - 1, target - arr[ind], arr) 
        unPickedCase = subsetSumEqTok(ind - 1, target, arr)  

        return (pickedCase or unPickedCase) 
    
arr = [2,3,4,5]
k = subsetSumEqTok(len(arr) - 1, 7, arr) 
print(k)  
