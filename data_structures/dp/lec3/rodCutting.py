def rodCutting(arr): 
    return rodCuttingRec(arr, len(arr), len(arr) - 1)


def rodCuttingRec(arr, remLength, index): 
    if (remLength == 0): 
        return 0 
    if (index == 0): 
        return remLength * arr[0] 
    notTaken = 0 + rodCuttingRec(arr, remLength, index - 1)
    taken = 0 
    if (remLength >= (index + 1)):
        taken = arr[index] + rodCuttingRec(arr, remLength - index - 1, index) 

    return max(taken, notTaken)
     

arr = [2,5,7,8,10] 
k = rodCutting(arr) 
print(k)