from collections import deque 

def zeroOneDist(ogMat):
    visitedMatrix = [[0 for _ in range(len(ogMat[0]))] for _ in range(len(ogMat))] 
    distanceMatrix = [[0 for _ in range(len(ogMat[0]))] for _ in range(len(ogMat))] 

    queue = deque() 

    for i in range(len(ogMat)): 
        for j in range(len(ogMat[0])): 
            if ogMat[i][j] == 1: 
                queue.append(i, j, 0) 
                visitedMatrix[i][j] = 1
            else: 
                visitedMatrix[i][j] = 0

    directions = [(0,1), (1,0), (-1, 0), (0, -1)]

    while queue: 
        row, col, steps = queue.popleft() 
        distanceMatrix[row][col] = steps

        for k in range(len(directions)): 
            dx, dy = k 
            nrow = row + dx 
            ncol = col + dy

            if nrow >= 0 and ncol >= 0 and ncol < len(ogMat[0]) and nrow < len(ogMat) and ogMat[nrow][ncol] == 0 and visitedMatrix[nrow][ncol] == 0: 
                queue.append((nrow, ncol, steps + 1)) 
                visitedMatrix[nrow][ncol] = 1 

    return distanceMatrix