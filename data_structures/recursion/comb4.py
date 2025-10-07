def combiSum(target, count, ds, val): 
    if (target == 0 and count == 0): 
        return [ds]

    if (target < 0 or count < 0):  
        return [] 

    res = []
    for i in range(val, 10):
        res += combiSum(target - i, count - 1, ds + [i], i + 1)
    return res



def combinationSum4(target, count): 
    return combiSum(target, count, [], 1) 

print(combinationSum4(9, 3))