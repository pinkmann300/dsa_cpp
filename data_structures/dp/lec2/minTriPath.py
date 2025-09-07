def minTriPath(row, col, grid): 
    if row == len(grid) - 1 : 
        return grid[row][col]
    if row < 0 or col > row: 
        return int(1e9) 
    else:
        down = grid[row][col] + minTriPath(row + 1, col, grid)
        diagonal = grid[row][col] + minTriPath(row + 1, col + 1, grid) 
        return min(down, diagonal) 
    

def minTriPath()
    

triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
n = len(triangle)

# Call the minimumPathSum function and print the result
print(minTriPath(0, 0, triangle))

