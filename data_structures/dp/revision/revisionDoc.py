""" 
First, we will look at the frog jump problem which is very similar to the 
Fibonacci problem. 
"""

def recursiveFrogJump1(heights, index): 
    if index == 0: 
        return 0 
    
    if index == 1: 
        return abs(heights[1] - heights[0]) 
    
    if index == 2: 
        return min(abs(heights[1] - heights[0]), abs(heights[2] - heights[0]))
    
    jump1 = recursiveFrogJump1(heights, index - 1) + abs(heights[index] - heights[index - 1]) 
    jump2 = recursiveFrogJump1(heights, index - 2) + abs(heights[index] - heights[index - 2]) 

    return min(jump1,  jump2)

def memoizedFrogJump(heights, index, dp): 
    if index == 0: 
        return 0 
    
    if index == 1: 
        return abs(heights[1] - heights[0]) 
    
    if dp[index] != -1: 
        return dp[index] 
    
    jump2 = float('inf') 

    jump1 = memoizedFrogJump(heights, index - 1, dp) + abs(heights[index] - heights[index - 1]) 
    if index > 1: 
        jump2 = memoizedFrogJump(heights, index - 2, dp) + abs(heights[index] - heights[index - 2]) 

    dp[index] = min(jump1, jump2) 
    return dp[index] 

def memoizedStartFJ(heights, index): 
    dp = [-1 for _ in range(len(heights))] 
    k = memoizedFrogJump(heights, index, dp) 

    return k 


def tabulationFrogJump(heights, index): 
    dp = [0 for _ in range(len(heights))] 
    dp[0] = 0 
    dp[1] = abs(heights[0] - heights[1]) 

    for i in range(2, index + 1): 
        jump1 = dp[i - 1] + abs(heights[i] - heights[i - 1]) 
        jump2 = dp[i - 2] + abs(heights[i] - heights[i - 2]) 

        dp[i] = min(jump1, jump2) 

    return dp[index] 



"""
 You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
 the only constraint stopping you
 from robbing each of them is that adjacent houses have security systems connected
 and it will automatically contact the police if two adjacent houses were broken into on the same night.
 Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""


def robRecursive(arr, ind):
    if ind < 0: 
        return 0  
    if ind == 0: 
        return arr[0] 
    else: 
        taken = arr[ind] + robRecursive(arr, ind - 2) 
        notTaken = robRecursive(arr, ind - 1)

        return max(taken, notTaken) 


def touchRec(arr, ind): 
    prev = arr[0]
    prev_2 = 0 

    for index in range(1, len(ind)): 
        pick = arr[index] 
        pick += prev_2 
        nonPick = prev 

        cur_i = max(pick, nonPick) 

    return prev 


def uniquePaths(m, n, row, col): 
    if row == 0 and col == 0: 
        return 1 
    
    if row < 0 or col < 0 or row >= m or col >= n: 
        return 0 

    up = uniquePaths(m, n,row - 1, col) 
    left = uniquePaths(m, n ,row, col - 1) 

    return up + left 

def uniquePathsMemoized(m, n): 
    dp = [[0 for _ in range(n)] for _ in range(n)] 

    dp[0][0] = 1 
    
    for i in range(1,m): 
        for j in range(1, n): 
            up = 0 
            left = 0 

            if i > 0:
                up = dp[i - 1][j] 

            if j > 0: 
                left = dp[i][j - 1] 

            dp[i][j] = up + left 

    return dp[m - 1][n - 1] 


def recSumTarget(arr, index, target): 
    if index < 0: 
        return False 
    
    if target == 0: 
        return True 
    
    if index == 0 and target == arr[index]: 
        return True 
    
    taken = False 

    if arr[index] <= target: 
        taken = recSumTarget(arr, index - 1, target - arr[index]) 
    notTaken = recSumTarget(arr, index - 1, target) 

    return taken or notTaken 


def tabulationSumTarget(arr, target): 
    dp = [[False for _ in range(target + 1)] for _ in range(len(arr))] 
    for i in range(len(arr)):
        dp[i][0] = True 

    dp[0][arr[0]] = True 

    for i in range(1, len(arr)): 
        for target1 in range(1, target + 1): 
            notTaken = dp[i - 1][target1] 

            taken = False 

            if arr[i] <= target1: 
                taken = dp[i - 1][target1 - arr[i]] 
            dp[i][target1] = notTaken or taken  

    return dp[len(arr) - 1][target]

def spaceOptimized(arr, target): 
    prev = [False for _ in range(target + 1)] 
    prev[0] = True 

    prev[arr[0]] = True 

    for i in range(1, len(arr)): 
        current = [False for _ in range(target + 1)] 
        current[0] = True 

        for target1 in range(1, target + 1): 
            notTaken = prev[target1] 
            taken = False 

            if arr[i] <= target1: 
                taken = prev[target1 - arr[i]] 
            current[target1] = notTaken or taken 

        prev = current[:] 

    return prev[target] 


""" 
Problem statement: 
Count the number of subsets with a sum of K. 
"""

"""
Recursive solution: 
"""

def recursiveCountSubsetK(arr, ind, target): 
    if target == 0: 
        return 1 
    
    if ind == 0: 
        if target == arr[ind]: 
            return 1 
        else: 
            return 0 
    
    else: 

        taken = 0 
        if arr[ind] <= target: 
            taken = recursiveCountSubsetK(arr, ind - 1, target - arr[ind]) 
        notTaken = recursiveCountSubsetK(arr, ind - 1, target) 

        return taken + notTaken 
    

def tabulationApproach(arr, target):
    dp = [[0 for _ in range(target + 1)] for _ in range(len(arr))] 
    for i in range(len(arr)): 
        dp[i][0] = 1 

    dp[0][arr[0]] = 1 

    for ind in range(1, len(arr)): 
        for targets in range(1, target + 1): 
            taken = 0 

            notTaken = dp[ind - 1][targets]  
            if arr[ind] <= targets: 
                taken = dp[ind - 1][targets - arr[ind]] 
            
            dp[ind][targets] = taken + notTaken 

    return dp[len(arr) - 1][target] 

#Handle the zero case in the edge cases.


