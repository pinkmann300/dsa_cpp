def uniqueWaysRec(grid, row, col): 
    if row == 0 and col == 0: 
        return 1 
    
    if row < 0 or col < 0: 
        return 0 
    
    left = uniqueWaysRec(grid, row, col - 1) 
    up = uniqueWaysRec(grid, row - 1, col) 

    return left + up 


