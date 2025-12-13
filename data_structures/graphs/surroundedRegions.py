""" 
Problem statement: 
Given a matrix mat of size N x M where every element is either 'O' or 'X'. Replace all 'O' with 'X' that is surrounded by 'X'. 
An 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 'X' at locations just below, just above just left, and just right of it.

Observation: 
The most important observation we can make here is that the presence of an 'O' on the boundary of the matrix would mean that any 'O' which will 
form a connected component with other 'O's nearby. So, we will run a DFS algorithm from the boundaries of the matrix.  
"""

def dfs(ogMat, visitMat, row, col):
    visitMat[row][col] = 1 
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] 
    n = len(ogMat) 
    m = len(ogMat[0])

    for i in directions: 
        dx, dy = i 
        nr = row + dx 
        nc = col + dy 

        if 0 <= nr < n and 0 <= nc < m and visitMat[nr][nc] == 0 and ogMat[nr][nc] == 'O': 
            dfs(ogMat, visitMat, nr, nc) 
         

def surroundedRegions(ogMat): 
    visitedMat = [[0 for _ in range(len(ogMat[0]))] for _ in range(len(ogMat))] 

    #Top boundary check: 
    for i in range(len(ogMat[0])): 
        if ogMat[0][i] == 'O' and visitedMat[0][i] == 0: 
            dfs(ogMat, visitedMat, 0, i)

        if ogMat[len(ogMat) - 1][i] == 'O' and visitedMat[len(ogMat) - 1][i] == 0:
            dfs(ogMat, visitedMat, len(ogMat) - 1, i)


    #Left and right boundary checks:

    for k in range(len(ogMat)): 
        if ogMat[k][0] == 'O' and visitedMat[k][0] == 0: 
            dfs(ogMat, visitedMat, k, 0) 

        if ogMat[k][len(ogMat[0]) - 1] == 'O' and visitedMat[k][len(ogMat[0]) - 1] == 0: 
            dfs(ogMat, visitedMat, k, len(ogMat[0]) - 1) 


    for row in range(len(ogMat)): 
        for col in range(len(ogMat[0])): 
            if visitedMat[row][col] == 0 and ogMat[row][col] == 0: 
                ogMat[row][col] = 'X' 