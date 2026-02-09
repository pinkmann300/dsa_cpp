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







    




