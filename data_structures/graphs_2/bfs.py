from collections import deque

def bfs(adjacencyList, V): 
    visited_array = [False for _ in range(V + 1)] 
    bfs_list = [] 

    for i in range(len(adjacencyList)): 
        if (visited_array[i]) == False: 
            visited_array[i] = True 
            que = deque() 
            que.append(i) 

            while que: 
                node = que.popleft() 
                bfs_list.append(node) 

                for nodes in adjacencyList[node]: 
                    if not visited_array[nodes]: 
                        visited_array[nodes] = True 
                        que.append(nodes) 

    return bfs_list       


def rottenOranges(matrix): 
    totalOranges = 0 
    rottenOranges = deque()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0: 
                if matrix[i][j] == 2: 
                    rottenOranges.append((i, j)) 
                totalOranges += 1 

    minutes = 0 
    rottenCount = 0 

    directionVectors = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

    while rottenOranges: 
        rottenCount += len(rottenOranges) 
        k = len(rottenOranges) 

        for _ in range(k): 
            rottenX, rottenY = rottenOranges.popleft()

            for dx, dy in directionVectors: 
                nx = rottenX + dx 
                ny = rottenY + dy 

                if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]) or matrix[nx][ny] != 1: 
                    continue 

                matrix[nx][ny] = 2 
                rottenOranges.append((nx, ny)) 

        if rottenOranges: 
            minutes += 1 


    return minutes if rottenCount == totalOranges else -1 
    









    
    

            
