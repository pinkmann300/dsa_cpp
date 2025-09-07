def minPathRec(grid, row, col, sum):
    if (row == 0 and col == 0):
        return sum + grid[row][col]
    
    if row < 0 or col < 0: 
        return float('inf') 
    
    else: 
        up = minPathRec(grid, row - 1, col, sum + grid[row][col])
        left = minPathRec(grid, row, col - 1, sum + grid[row][col])

        return min(up, left)
    

matrix = [[5, 9, 6],
              [11, 5, 2]]

n = len(matrix)
m = len(matrix[0])

print(minPathRec(matrix, n - 1, m - 1, 0))