def dfs(ogMat, visitedMat, row, col):
    visitedMat[row][col] = 1 

    directionVectors = [(0,1) , (0, -1), (1,1), (-1,-1), (1,0), (-1, 0), (1, -1), (-1,1)] 

    for dx, dy in directionVectors: 
        nx = row + dx 
        nc = col + dy

        if 0 <= nx < len(ogMat) and 0 <= nc < len(ogMat[0]) and visitedMat[nx][nc] == 0 and ogMat[nx][nc] == 1: 
            dfs(ogMat, visitedMat, nx, nc) 


def numberOfIslands(ogMat):
    visitedMatrix = [[0 for _ in range(len(ogMat[0]))] for _ in range(len(ogMat))] 
    count = 0

    for i in range(len(ogMat)): 
        for j in range(len(ogMat[0])): 
            if visitedMatrix[i][j] == 0 and ogMat[i][j] == 1: 
                dfs(ogMat, visitedMatrix, i, j) 
                count += 1 
    
    return count
