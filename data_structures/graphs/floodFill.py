from collections import deque


def floodFill(grid, sr, sc, color): 

    originalColor = grid[sr][sc] 
    if originalColor == color: 
        return grid 
    

    queue = deque() 
    queue.append((sr, sc))
    grid[sr][sc] = color


    movementVectors = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

    while queue: 
        x, y = queue.popleft() 
        
        for dx, dy in movementVectors: 
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != originalColor: 
                continue 
                
            if grid[nx][ny] == originalColor: 
                grid[nx][ny] = color
                queue.append((nx, ny))  

    return grid




