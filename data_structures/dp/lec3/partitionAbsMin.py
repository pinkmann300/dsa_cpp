def partitionAbsMinRec(arr, index, sum1):
    if (index == 0): 
        return abs(sum1 - (sum(arr) - sum1))
    taken = partitionAbsMinRec(arr, index - 1, sum1 + arr[index]) 
    notTaken = partitionAbsMinRec(arr, index - 1, sum1) 
    return min(taken, notTaken) 


def partitionStarter(arr): 
    totalSum = sum(arr) 
    dp = [[-1 for _ in range(totalSum + 1)] for _ in range(len(arr))]  
    for k in range(0, totalSum + 1):  
        dummy = partitionMemoizer(arr, len(arr) - 1, k, dp) 
    mini = int(1e9)
    for l in range(0, totalSum): 
        if dp[len(arr) - 1][l]: 
            diff = abs(l - (totalSum - l)) 
            mini = min(diff, mini) 
    return mini 


def partitionMemoizer(arr, ind, sum1, dp): 
    if (sum1 == 0): 
        return True 
    if (ind == 0 and arr[ind] == sum1): 
        return True 
    if (ind < 0): 
        return False 
    print(sum1)
    if (dp[ind][sum1] != -1): 
        return dp[ind][sum1] 
    taken = False 
    if (arr[ind] <= sum1): 
        taken = partitionMemoizer(arr, ind -1 , sum1 - arr[ind], dp) 
    notTaken = partitionMemoizer(arr, ind - 1, sum1, dp)  
    dp[ind][sum1] = taken or notTaken
    return dp[ind][sum1] 




arr = [1, 2, 3, 4]
print("The minimum absolute difference is:",partitionStarter(arr)) 
