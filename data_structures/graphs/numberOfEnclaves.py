def dfs(ogMat, visitedMatrix, row, col): 
    visitedMatrix[row][col] = 1
    dirVectors = [(0, 1), (1, 0), (-1, 0), (0, -1)] 

    for k in dirVectors: 
        dx, dy = k  
        nr = row + dx 
        nc = col + dy 

        if 0 <= nr < len(ogMat) and 0 <= nc < len(ogMat[0]) and visitedMatrix[nr][nc] == 0 and ogMat[nr][nc] == 1: 
            dfs(ogMat, visitedMatrix, nr, nc) 


def numberOfEnclaves(ogMat):
    visitedMatrix = [[0 for _ in range(len(ogMat[0]))] for _ in range(len(ogMat))] 

    for i in range(len(ogMat[0])): 
        if visitedMatrix[0][i] == 0 and ogMat[0][i] == 1: 
            dfs(ogMat, visitedMatrix, 0, i) 

        if visitedMatrix[len(ogMat) - 1][i] == 0 and ogMat[len(ogMat) - 1][i] == 1: 
            dfs(ogMat, visitedMatrix, len(ogMat) - 1, i) 

    
    for j in range(len(ogMat)):
        if visitedMatrix[j][0] == 0 and ogMat[j][0] == 1: 
            dfs(ogMat, visitedMatrix, j, 0) 

        if visitedMatrix[j][len(ogMat[0]) - 1] == 0 and ogMat[j][len(ogMat[0]) - 1] == 1: 
            dfs(ogMat, visitedMatrix, j, len(ogMat[0])  - 1) 

    total = 0 

    for row in range(len(ogMat)): 
        for col in range(len(ogMat[0])): 
            if visitedMatrix[row][col] == 0 and ogMat[row][col] == 1: 
                total += 1 

    return total 
