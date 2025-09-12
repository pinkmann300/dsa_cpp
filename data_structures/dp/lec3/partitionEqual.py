def partitionSubsetHelper(arr): 
    totalSum = sum(arr) 
    if (totalSum % 2 == 1): 
        return False 
    else:
        partitionSum = totalSum // 2 
        print(partitionSum)
        k = partitionMemoStart(partitionSum, len(arr) - 1, arr) 
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


arr = [2,3,3,3,4,5] 
l = partitionSubsetHelper(arr) 
print(l) 

