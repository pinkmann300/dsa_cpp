def knapsack(index, weight, weights, vals): 
    if (weight == 0): 
        return 0 
    if (index == 0): 
        if (weights[index] <= weight): 
            return vals[index] 
        else: 
            return 0 
    notTaken = 0 + knapsack(index - 1, weight, weights, vals) 
    taken = -1 
    if (weights[index] <= weight): 
        taken = vals[index] + knapsack(index - 1, weight - weights[index], weights, vals) 

    return max(taken, notTaken) 



wt = [5, 4, 2, 3]
val = [10, 40, 30, 50] 
weight = 5

print(knapsack(len(wt) - 1, weight, wt, val)) 
