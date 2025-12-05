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


def dfsStart(adjacencyList): 
    visited_arr = [0 for _ in range(len(adjacencyList))] 
    resultArr = [] 
    dfsOnGraph(0, adjacencyList, resultArr, visited_arr) 
    return resultArr



def dfsOnGraph(startingNode, adjacencyList, resultArr, visited): 
    visited[startingNode] = 1 
    resultArr.append(startingNode) 

    for i in adjacencyList[startingNode]: 
        if visited[i] == 0: 
            dfsOnGraph(i, adjacencyList, resultArr, visited)

    


def main(): 
    V = 5

    # Adjacency list
    adj = [[] for _ in range(V + 1)]
    adj[0] = [1,2]
    adj[1] = [0, 3]
    adj[2] = [0, 4]
    adj[3] = [1]
    adj[4] = [2]

    # Run DFS from node 0
    newArr = dfsStart(adj)
    print(newArr)
 

            

main(); 