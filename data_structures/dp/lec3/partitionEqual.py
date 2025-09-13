def partitionSubsetHelper(arr): 
    totalSum = sum(arr) 
    if (totalSum % 2 == 1): 
        return False 
    else:
        partitionSum = totalSum // 2 
        print(partitionSum)
        k = partitionTabulation(partitionSum, len(arr) - 1, arr) 
        return k 

def partitionFinder(sum1, ind, arr): 
    if (sum == 0): 
        return True 
    if (ind == 0 and arr[ind] == sum1): 
        return True 
    if (ind < 0) : 
        return False 
    taken = False 

    if (arr[ind] <= sum1):
        taken = partitionFinder(sum1 - arr[ind], ind - 1, arr) 
    
    notTaken = partitionFinder(sum1, ind - 1, arr) 

    return taken or notTaken

def partitionMemoizer(sum1, ind, arr, dp): 
    if (sum1 == 0): 
        return True 
    if (ind == 0 and arr[ind] == sum1): 
        return True 
    if (ind < 0): 
        return False 
    if (dp[ind][sum1] != -1): 
        return dp[ind][sum1] 
    taken = False 
    if (arr[ind] <= sum1): 
        taken = partitionMemoizer(sum1 - arr[ind], ind -1 , arr, dp) 
    notTaken = partitionMemoizer(sum1, ind - 1, arr, dp)  
    dp[ind][sum1] = taken or notTaken
    return dp[ind][sum1] 
 
def partitionMemoStart(sum1, ind, arr): 
    dp = [[-1 for _ in range(sum1 + 1)] for _ in range(ind + 1)] 
    finalResult = partitionMemoizer(sum1, ind, arr, dp) 
    return finalResult

def partitionTabulation(sum1, ind, arr):
    dp = [[False for _ in range(sum1 + 1)] for _ in range(ind + 1)] 
    for index in range(ind + 1): 
        dp[index][0] = True 
    if (arr[0] <= sum1): 
        dp[0][arr[0]] = True 
    for row in range(1,ind + 1): 
        for column in range(1, sum1 + 1): 
            taken = False 
            notTaken = dp[row - 1][column] 
            if (arr[row] <= column): 
                taken = dp[row - 1][column - arr[row]]
            dp[row][column] = taken or notTaken 
    return dp[ind][sum1] 

arr = [2,3,3,3,4,5] 
l = partitionSubsetHelper(arr) 
print(l) 

