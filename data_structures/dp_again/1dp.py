def maxSumNonA(arr, i): 
    if i < 0: 
        return 0
    
    if i == 0: 
        return arr[0] 
    else: 
        take = arr[i] + maxSumNonA(arr, i - 2) 
        noTake = maxSumNonA(arr, i - 1) 

        return max(take, noTake)


def tabulatedSolution(arr): 
    dp = [0 for _ in range(len(arr))] 
    dp[0] = arr[0] 

    for i in range(1, len(arr)): 
        take = float('-inf')
        notake = dp[i - 1] 
        if i > 1:
            take = dp[i - 2] + arr[i] 

        dp[i] = max(take, notake) 

    return dp[-1] 

def houseRobber(arr): 
    firstPart = tabulatedSolution(arr[1:]) 
    secondPart = tabulatedSolution(arr[:len(arr) - 1])

    return max(firstPart , secondPart)