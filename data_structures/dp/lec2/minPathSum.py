def minPathRec(grid, row, col, sum):
    if (row == 0 and col == 0):
        return sum + grid[row][col]
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

    

def main():
    # Example matrix with values representing cell costs.
    matrix = [[5, 9, 6],
              [11, 5, 2]]
    
   

    n = len(matrix)
    m = len(matrix[0])
    dp = [[-1 for j in range(m)] for i in range(n)]

    # Call the minSumPath function and print the result.
    print(minPathMemo(matrix, n - 1, m - 1, dp))


if __name__ == '__main__':
    main()