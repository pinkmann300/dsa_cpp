def maxPath(row,  col,  matrix): 
    if (row == 0 and col >= 0 and col < len(matrix[0])): 
        return matrix[row][col]
    if (row < 0 or col < 0 or col >= len(matrix[0]) or row >= len(matrix)): 
        return int(-1e9)
    
    up = int(-1e9) 
    leftDiagonal = int(-1e9) 
    upperDiagonal = int(-1e9) 

    if (row > 0): 
        up = matrix[row][col] + maxPath(row - 1, col, matrix) 

    if (col > 0 and row > 0): 
        leftDiagonal = matrix[row][col] + maxPath(row - 1, col - 1, matrix) 

    if (col < len(matrix[0]) - 1 and row > 0): 
        upperDiagonal = matrix[row][col] + maxPath(row - 1, col + 1, matrix) 

    return max(up, max(leftDiagonal, upperDiagonal)) 


def maxPathMemo(row, col, matrix, dp): 
    if (row == 0 and col >= 0 and col < len(matrix[0])): 
        return matrix[row][col] 

    if (row < 0 or col < 0 or col >= len(matrix[0]) or row >= len(matrix)): 
        return int(-1e9) 
    
    if (dp[row][col] != -1): 
        return dp[row][col] 
    
    up = int(-1e9) 
    leftDiagonal = int(-1e9) 
    upperDiagonal = int(-1e9) 

    if (row > 0): 
        up = matrix[row][col] + maxPathMemo(row - 1, col, matrix, dp) 

    if (col > 0 and row > 0): 
        leftDiagonal = matrix[row][col] + maxPathMemo(row - 1, col - 1, matrix, dp) 

    if (col < len(matrix[0]) - 1 and row > 0): 
        upperDiagonal = matrix[row][col] + maxPathMemo(row - 1, col + 1, matrix, dp) 

    dp[row][col] = max(up, max(leftDiagonal, upperDiagonal)) 
    return dp[row][col] 

def maxPathTab(matrix): 
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))] 
    for i in range(len(matrix[0])): 
        dp[0][i] = matrix[0][i]

    for row in range(1, len(matrix)): 
        for j in range(len(matrix[0])):
            up = dp[row - 1][j] + matrix[row][j]
            diagDown = int(-1e9) 
            leftDiag = int(-1e9)
            
            if j > 0:
                diagDown = dp[row - 1][j - 1] + matrix[row][j]
            
            if j < len(matrix[0]) - 1: 
                leftDiag = dp[row - 1][j + 1] + matrix[row][j]
            
            dp[row][j] = max(up, max(diagDown, leftDiag))
    maxi = 0 
    for k in range(len(matrix[0])): 
        maxi = max(maxi, dp[len(matrix) - 1][k]) 
    return maxi     

def maxPathFinal(matrix):
    dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    maxPathSum = int(-1e9) 
    for j in range(0, len(matrix[0])): 
        newMax = maxPathMemo(len(matrix) - 1, j, matrix, dp) 
        maxPathSum = max(newMax, maxPathSum) 

    return maxPathSum



matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
k = maxPathTab(matrix) 
print(k) 