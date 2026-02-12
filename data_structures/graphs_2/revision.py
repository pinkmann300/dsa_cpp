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





    