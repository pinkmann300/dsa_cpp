""" 
Assuming the graph using 0 based indexing
"""

def createAdjacenyList(numberOfVertices, edges):
    adjacencyList = [[] for _ in range(numberOfVertices)] 

    for [start, end] in edges: 
        adjacencyList[start].append(end) 
        adjacencyList[end].append(start) 

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