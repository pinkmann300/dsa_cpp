def minPathRec(grid, row, col, sum):
    if (row == 0 and col == 0):
        return sum + grid[0][0]
    if row < 0 or col < 0: 
        return float('inf') 
    else: 
        up = minPathRec(grid, row - 1, col, sum + grid[row][col])
        left = minPathRec(grid, row, col - 1, sum + grid[row][col])
        return min(up, left)
    
def minPathMemo(grid, row, col, dp):
    if row == 0 and col == 0: 
        return (grid[0][0])
    if row < 0 or col < 0:
        return int(1e9)
    if dp[row][col] != -1: 
        return dp[row][col]
    
    up = grid[row][col] + minPathMemo(grid, row - 1, col, dp)
    left = grid[row][col] + minPathMemo(grid, row, col - 1, dp)
    dp[row][col] = min(up, left)

    return dp[row][col]

    
def minPathTabulation(row, col, grid): 
    dp = [[-1] * len(grid[0])] * len(grid) 
    for i in range(row):
        for j in range(col): 
            if i == 0 and j == 0: 
                dp[i][j] = grid[0][0]
                continue 

            up = int(1e9)
            left = int(1e9)

            if i > 0: 
                up = dp[i - 1][j] + grid[i][j] 
            
            if j > 0: 
                left = dp[i][j - 1] + grid[i][j] 

            dp[i][j] = min(up, left) 
    return dp[row - 1][col - 1]


def main():
    # Example matrix with values representing cell costs.
    matrix = [[5, 9, 6],
              [11, 5, 2]]
    
    n = len(matrix)
    m = len(matrix[0])
    dp = [[-1 for j in range(m)] for i in range(n)]

    # Call the minSumPath function and print the result.
    print(minPathTabulation( n , m , matrix))


if __name__ == '__main__':
    main()