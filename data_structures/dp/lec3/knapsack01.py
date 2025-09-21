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


def knapsackTab(weight, weights, val): 
    dp = [[0 for _ in range(weight + 1)] for _ in range(len(weights))]
    for i in range(weight + 1): 
        if (i >= weights[0]):
            dp[0][i] = val[0] 
    ans = 0 
    for index2 in range(1, len(weights)): 
        for weightIndex in range(weight + 1):
            taken = -1 
            notTaken = dp[index2 - 1][weightIndex] 
            if (weights[index2] <= weightIndex): 
                taken = val[index2] +  dp[index2 - 1][weightIndex - weights[index2]]
            dp[index2][weightIndex] = max(taken, notTaken) 
            ans = max(dp[index2][weightIndex], ans) 
    

    return dp[len(weights)-1][weight] 


wt = [1, 7, 9]
val = [10,8,6] 
weight = 7

print(knapsackTab(weight, wt, val)) 
