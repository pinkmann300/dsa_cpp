def countSubsets(arr, index, target): 
    if (target == 0): 
        return 1 
    if (index == 0 and arr[0] == target): 
        return 1 
    if (index < 0): 
        return 0
    
    taken = 0 
    if arr[index] <= target: 
        taken = countSubsets(arr, index - 1, target - arr[index]) 
    notTaken = countSubsets(arr, index - 1, target) 

    return taken + notTaken 

arr = [1,2,2,3] 
print(countSubsets(arr, len(arr) - 1, 4)) 
