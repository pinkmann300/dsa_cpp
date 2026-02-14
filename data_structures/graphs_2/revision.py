from collections import deque

""" 
Assuming the graph using 0 based indexing
"""

def createAdjacenyList(numberOfVertices, edges):
    adjacencyList = [[] for _ in range(numberOfVertices)] 

    for [start, end] in edges: 
        adjacencyList[start].append(end) 
        adjacencyList[end].append(start) 

    return adjacencyList 


def createAdjacencyListFromMatrix(matrix): 
    adjacencyList = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)): 
        for j in range(len(matrix)): 
            if matrix[i][j] == 1: 
                adjacencyList[i].append(j) 
    
    return adjacencyList
 
def dfsStart(adjacencyList): 
    visitedArray = [0 for _ in range(len(adjacencyList))] 
    resultantArray = [] 

    for i in range(len(adjacencyList)): 
        if visitedArray[i] != 1: 
            dfs(adjacencyList, i, visitedArray, resultantArray) 

    return resultantArray


def dfs(adjacencyList, srcNode, visitedArray, resultant): 
    visitedArray[srcNode] = 1 
    resultant.append(srcNode)

    for adjNodes in adjacencyList[srcNode]: 
        if visitedArray[adjNodes] != 1: 
            dfs(adjacencyList, adjNodes, visitedArray, resultant)


def numberOfProvinces(connectionMatrix): 
    adjacencyList = createAdjacencyListFromMatrix(connectionMatrix) 
    visitedArray = [0 for _ in range(len(adjacencyList))] 
    count = 0 

    for i in range(len(adjacencyList)): 
        if visitedArray[i] != 1: 
            queue = deque() 
            queue.append(i) 

            while queue:
                node = queue.popleft() 
                visitedArray[node] = 1 

                for adjNodes in adjacencyList[node]:
                    if visitedArray[adjNodes] != 1: 
                        queue.append(adjNodes) 

        count += 1 

    return count 

def rottenOranges(orangesGrid):
    directionVectors = [(0,1 ), (0, -1), (-1, 0), (1, 0)] 
    queue = deque()
    totalOranges = 0 
    rottenOranges = 0 
    time = 0 

    for i in range(len(orangesGrid)): 
        for j in range(len(orangesGrid[0])): 
            if orangesGrid[i][j] != 0:
                totalOranges += 1 
                if orangesGrid[i][j] == 2: 
                    queue.append((i, j)) 

    while queue:
        rottenOranges += len(queue)  
        for k in range(len(queue)):
            x, y = queue.popleft() 

            for dx, dy in directionVectors: 
                nx = dx + x 
                ny = dy + y 

                if nx >= 0 and nx < len(orangesGrid) and ny >= 0 and ny < len(orangesGrid[0]) and orangesGrid[nx][ny] == 1: 
                    orangesGrid[nx][ny] = 2 
                    queue.append((nx, ny)) 
        if queue: 
            time += 1 

    return time if rottenOranges == totalOranges else -1 


def floodFill(grid, sourceRow, sourceCol, newColor): 
    originalColor = grid[sourceRow][sourceCol] 
    if grid[sourceRow][sourceCol] == newColor: 
        return 
    
    travQueue = deque()
    travQueue.append((sourceRow, sourceCol)) 

    directionVectors = [(0,1), (1, 0), (-1, 0), (0, -1)] 
    
    while travQueue:
        x, y = travQueue.popleft() 
        grid[x][y] = newColor 

        for dx, dy in directionVectors: 
            nx = dx + x 
            ny = dy + y 

            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == originalColor: 
                travQueue.append((nx, ny)) 

    return grid     


def detectCycle(adjacencyList): 
    travQueue = deque() 
    visitedArray = [0 for _ in range(len(adjacencyList))] 


    for i in range(len(adjacencyList)): 
        travQueue.append((i, None))  
        while travQueue: 
            node, parent = travQueue.popleft() 
            visitedArray[node] = 1 

            for adjNodes in adjacencyList[node]: 
                if visitedArray[adjNodes] == 0: 
                    travQueue.append((adjNodes, node)) 
                elif (adjNodes != parent): 
                    return True
                
    return False      


def topoLogicalSort(adjacencyList): 
    indegree = [0] * len(adjacencyList) 
    topoSort = []

    for i in range(len(adjacencyList)): 
        for k in adjacencyList[i]: 
            indegree[k] += 1 

    queue = deque() 

    for k in range(len(indegree)): 
        if indegree[k] == 0: 
            queue.append(k) 

    while queue: 
        node = k.popleft() 
        topoSort.append(node) 

        for m in adjacencyList[node]:
            indegree[m] -= 1 
            if indegree[m] == 0:
                queue.append(m) 

    
    return topoSort