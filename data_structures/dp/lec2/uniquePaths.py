def uniqueGridPaths(row, col):
    if (row == 0) and (col == 0): 
        return 1 
    if (row < 0) or (col < 0): 
        return 0 
    k = uniqueGridPaths(row - 1, col) # Moving up 
    r = uniqueGridPaths(row, col - 1)
    return k + r 

# The above solution is a recursive implementation of the function to compute 
# the number of ways you can reach the edge of the grid.

def uniqueGridPathsMemoized(row, col, dp):
    if (row == 0 and col == 0): 
        return 1 
    if (row < 0 or col < 0):
        return 0 
    if (dp[row][col] != -1):
        return dp[row][col]
    up = uniqueGridPathsMemoized(row - 1, col, dp)
    left = uniqueGridPathsMemoized(row, col - 1, dp)
    dp[row][col] = up + left
    print(dp)
    return dp[row][col]


def uniqueGridPathTabulation(row, col):
    dp = [[-1] * col] * row
    for i in range(row): 
        for j in range(col):
            if (i == 0 and j == 0): 
                dp[i][j] = 1 
                continue
            up = 0 
            left = 0 

            if i > 0: 
                up = dp[i - 1][j] 
            
            if j > 0: 
                left = dp[i][j - 1]

            dp[i][j] = up + left

    print(dp)
    return dp[row - 1][col - 1]


k = uniqueGridPathTabulation(2,3)
print(k)