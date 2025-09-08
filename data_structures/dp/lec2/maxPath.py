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


def maxPathFinal(matrix): 
    maxPathSum = int(-1e9) 
    for j in range(0, len(matrix[0])): 
        newMax = maxPath(len(matrix) - 1, j, matrix) 
        maxPathSum = max(newMax, maxPathSum) 

    return maxPathSum



matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
k = maxPathFinal(matrix) 
print(k) 