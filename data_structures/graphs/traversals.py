from collections import deque

"""
The following python document will store information and other theory required to 
traverse through a graph along the breadth or level order traversal. 

Given: a graph, a starting node. First you visit the first guy and then visit the dudes
at the next level. 
"""

def createAdjacencyList(vertices, edges, edgeList):
    adjList = [[] for _ in range(vertices + 1)] 
    for i in range(0, edges): 
        node1, node2 = edgeList[i] 
        adjList[node1].append(node2)
        adjList[node2].append(node1) 

    return adjList 

def bfsOnGraph(adjacencyList, startingNode): 
    bfsArray = []
    visited_array = [0 for _ in range(len(adjacencyList))] 
    visited_array[0] = 1

    queue = deque() 
    queue.append(startingNode)
    visited_array[startingNode] = 1 

    while queue: 
        node = queue.popleft() 
        bfsArray.append(node) 

        for k in adjacencyList[node]:
            if visited_array[k] != 1: 
                queue.append(k) 
                visited_array[k] = 1 

    return bfsArray
        

def dfsOnGraph(adjacenyList, startingNode): 
    pass 
 

            
