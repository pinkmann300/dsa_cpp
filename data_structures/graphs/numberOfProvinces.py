"""

Problem Statement: Given an undirected graph with V vertices. Two vertices u and v belong to a single province if 
there is a path from u to v or v to u. Find the number of provinces. The graph is given as an n x n matrix adj where
adj[i][j] = 1 if the ith city and the jth city are directly connected, and adj[i][j] = 0 otherwise.

Examples

Input: adj=[ [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1] ]
Output: 2
Explanation: In this graph, there are two provinces: [1, 4] and [2, 3]. City 1 and city 4 have a path between them, 
and city 2 and city 3 also have a path between them. There is no path between any city in province 1 and any city in province 2.

Input: adj= [ [1, 0, 1], [0, 1, 0], [1, 0, 1] ]
Output: 2
Explanation :  The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between them they belong to a 
single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.
            
"""


"""
Solution explanation:  
In some sense, the number of provinces will be equal to the number of connected components in a graph. When we perform DFS, we 
are able to traverse through all the nodes in one particular connected component. We need to find out how many times we have to 
perform DFS in order to mark all the nodes in the visited array. That would determine the number of provinces in a given undirected graph. 
"""


def dfs(startingNode, resultArr, visited_arr, adjacencyList): 
    visited_arr[startingNode] = 1 
    resultArr.append(startingNode) 

    for i in adjacencyList[startingNode]: 
        if visited_arr[i] != 1: 
            dfs(i, resultArr, visited_arr, adjacencyList) 
    

def numberOfProvinces(adjacencyMatrix): 
    numberOfVertices = len(adjacencyMatrix)
    adjacencyList = [[] for _ in range(len(adjacencyMatrix))] 

    for i in range(numberOfVertices): 
        for j in range(numberOfVertices):
            if adjacencyMatrix[i][j] and i != j: 
                adjacencyList[i].append(j) 
                adjacencyList[j].append(i) 

    visited_arr = [0 for _ in range(len(adjacencyList))] 
    result_arr = []

    provinceCount = 0 

    for i in range(numberOfVertices): 
        if visited_arr[i] == 0: 
            dfs(i, result_arr, visited_arr, adjacencyList) 
            provinceCount += 1 

    return provinceCount

