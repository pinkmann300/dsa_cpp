def minTriPath(row, col, grid): 
    if row == len(grid) - 1 : 
        return grid[row][col]
    if row < 0 or col > row: 
        return int(1e9) 
    else:
        down = grid[row][col] + minTriPath(row + 1, col, grid)
        diagonal = grid[row][col] + minTriPath(row + 1, col + 1, grid) 
        return min(down, diagonal) 
    

def minTriPathMemo(row, col, grid, dp):
    if (dp[row][col] != -1): 
        return dp[row][col] 
    if (row == (len(grid) - 1) ): 
        return grid[row][col]
    down = grid[row][col] + minTriPathMemo(row + 1, col, grid, dp) 
    diagonal = grid[row][col] + minTriPathMemo(row + 1, col + 1, grid, dp) 
    dp[row][col] = min(down, diagonal)
    return dp[row][col]


def minTriPathTab(row, col, grid): 
    dp = [[-1 for _ in range(len(grid))] for _ in range(len(grid))]
    for i in range(len(grid)): 
        for j in range(len(grid)): 
            if i == 0 and j == 0: 
                dp[i][j] = grid[i][j]
                continue

            down = int(1e9) 
            diagonal = int(1e9) 

            if (i > 0): 
                down = dp[i - 1][j] + grid[i][j] 
            
            if (j > 0): 
                diagonal = dp[i - 1][j - 1] + grid[i][j] 

            finVal = min(down, diagonal) 
            dp[i][j] = finVal 

    return dp[row - 1][col - 1]    

triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
n = len(triangle)
dp = [[-1 for _ in range(n)] for _ in range(n)]
# Call the minimumPathSum function and print the result
print(minTriPathTab(n, n, triangle))

