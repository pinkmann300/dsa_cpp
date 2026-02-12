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


        

