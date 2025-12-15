def dfs(node, col, adjList, coloredArray): 
    coloredArray[node] = col 
    for k in adjList[node]: 
        newCol = 1 if col == 0 else 0 
        if coloredArray[k] == -1: 
            if (not dfs(k, newCol, adjList, coloredArray)):
                return False
        else: 
            if coloredArray[k] == col: 
                return False     
    return True 

        

def bipartite(adjList): 
    coloredArray = [-1 for _ in range(len(adjList))] 

    for i in range(len(adjList)): 
        if coloredArray[i] == -1: 
            if (dfs(i, 0, adjList, coloredArray) == False): 
                return False 
            
    return True 




