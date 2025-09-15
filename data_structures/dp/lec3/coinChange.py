def coinChangeCount(arr, target): 
    return coinChangeCountRec(arr, target, len(arr) - 1) 

def coinChangeCountRec(arr, target, index): 
    if (index == 0): 
        if (target == 0 and arr[0] == 0): 
            return 2 
        if (target == 0 or target % arr[0] == 0): 
            return 1 
        return 0 
    
    notTaken = coinChangeCountRec(arr, target, index - 1)
    taken = 0 
    if (arr[index] <= target): 
        taken = coinChangeCountRec(arr, target - arr[index], index) 
    return taken + notTaken
 
arr = [1,2,3] 
target = 4 

print(coinChangeCount(arr, target)) 
