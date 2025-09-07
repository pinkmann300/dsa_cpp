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

    

def minSumPathUtil(i, j, matrix, dp):
    # Base case: If we are at the top-left corner, return the value of that cell.
    if i == 0 and j == 0:
        return matrix[0][0]
    
    # Base case: If we are out of bounds (negative indices), return a very large value.
    if i < 0 or j < 0:
        return int(1e9)
    
    # If we have already calculated the minimum sum for this cell, return it.
    if dp[i][j] != -1:
        return dp[i][j]

    # Calculate the minimum sum path recursively by considering both up and left moves.
    up = matrix[i][j] + minSumPathUtil(i-1, j, matrix, dp)
    left = matrix[i][j] + minSumPathUtil(i, j-1, matrix, dp)

    # Store the minimum of the two possible paths in the DP table.
    dp[i][j] = min(up, left)
    return dp[i][j]


def minSumPath(n, m, matrix):
    # Create a DP table initialized with -1 values.
    dp = [[-1 for j in range(m)] for i in range(n)]
    
    # Call the utility function to find the minimum sum path.
    return minSumPathUtil(n-1, m-1, matrix, dp)


def main():
    # Example matrix with values representing cell costs.
    matrix = [[5, 9, 6],
              [11, 5, 2]]

    n = len(matrix)
    m = len(matrix[0])

    # Call the minSumPath function and print the result.
    print(minSumPath(n, m, matrix))


if __name__ == '__main__':
    main()