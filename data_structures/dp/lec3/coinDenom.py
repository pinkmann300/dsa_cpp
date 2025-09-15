def coinDenom(arr, target): 
    return coinDenomRec(arr, target, len(arr) - 1)

def coinDenomRec(arr, target, index): 
    if (target == 0): 
        return 0 
    if index == 0 :
        if (target % arr[index] == 0):
            return target // arr[index] 
        else: 
            return int(1e9) 
    taken = int(1e9) 
    if (arr[index] <= target): 
        taken = 1 + coinDenomRec(arr, target - arr[index], index) 
    notTaken = coinDenomRec(arr, target, index - 1) 
    return min(taken, notTaken) 
    
arr = [1,2,3] 
target = 7 
print(coinDenom(arr, target))