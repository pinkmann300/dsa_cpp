from collections import deque

"""
Problem Statement: 
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.
"""


def rottenOranges(adjacencyMatrix):
    time = 0 
    totalOranges = 0 
    rottenOranges = 0 

    rotten = deque() 

    for i in range(len(adjacencyMatrix)): 
        for j in range(len(adjacencyMatrix[0])): 
            if adjacencyMatrix[i][j] != 0: 
                totalOranges += 1 

            if adjacencyMatrix[i][j] == 2: 
                rotten.append((i, j)) 

    movementVector = [(-1,0), (1, 0), (0, 1), (0, -1)] 

    while rotten: 
        
        k = len(rotten) 
        rottenOranges += k
        for _ in range(k): 
            x, y = rotten.popleft() 

            for dx, dy in movementVector: 
                nx, ny = x + dx, y + dy 

                if nx < 0 or ny < 0 or adjacencyMatrix[nx][ny] != 1 or nx >= len(adjacencyMatrix)  or ny >= len(adjacencyMatrix[0]):
                    continue 

                adjacencyMatrix[nx][ny] = 2 
                rotten.append((nx, ny)) 

        if rotten: 
            time += 1 

    return time if rottenOranges == totalOranges else -1 