def subsetSumCheck(index, target, arr): 
    if target == 0: 
        return True 
    
    if index == len(arr): 
        return False 
    
    taken = False 
    notTaken = subsetSumCheck(index + 1, target, arr) 

    if arr[index] <= target: 
        taken = subsetSumCheck(index + 1, target - arr[index], arr) 

    return taken or notTaken 


def mainSubsetSum(target, arr): 
    return subsetSumCheck(0, target, arr) 

arr = [1,2,3,4] 
print(mainSubsetSum(15, arr)) 

