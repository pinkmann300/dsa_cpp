def uniqPathRec(grid, row, col): 
    if (grid[row][col] == -1): 
        return 0 
    
    if (row == 0 and col == 0): 
        return 1 
    
    if (row < 0 or col < 0):
        return 0 
    
    else: 
        up = uniqPathRec(grid, row - 1, col)
        left = uniqPathRec(grid, row, col - 1) 

        return up + left  
    

def uniqPathMemo(grid, row, col, dp): 
    if (grid[row][col] == -1): 
        return 0 
    
    if (row == 0 and col == 0):
        return 1 
    
    if (row < 0 or col < 0): 
        return 0 
    
    if (dp[row][col] != -1): 
        return dp[row][col]
    
    else: 
        up = uniqPathMemo(grid, row - 1, col, dp)
        left = uniqPathMemo(grid, row, col - 1, dp)
        dp[row][col] = up + left 
        return dp[row][col]
    

def uniqPathsTabulation(grid, row, col): 
    dp = [[-1] * col] * row 
    for i in range(row): 
        for j in range(col):    
            if grid[i][j] == -1:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0: 
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
    return dp[row-1][col - 1] 
            

            
    

dp = [[-1] * 3] * 3 
maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
n = len(maze)
m = len(maze[0])

    # Call the mazeObstacles function and print the result.
print(uniqPathMemo(maze,n - 1, m - 1, dp))

print(uniqPathsTabulation(maze, n, m))