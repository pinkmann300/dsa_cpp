""" 
Assuming the graph using 0 based indexing
"""

def createAdjacenyList(numberOfVertices, edges):
    adjacencyList = [[] for _ in range(numberOfVertices)] 

    for [start, end] in edges: 
        adjacencyList[start].append(end) 
        adjacencyList[end].append(start) 

    return adjacencyList 

    
    