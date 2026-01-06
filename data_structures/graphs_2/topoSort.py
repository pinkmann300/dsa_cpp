from collections import deque 

def dfs(adjList, visitedArray, stack, index): 
    visitedArray[index] = 1 

    for adjNodes in adjList[index]: 
        if visitedArray[adjNodes] == 0:
            dfs(adjList, visitedArray, stack, adjNodes) 

    stack.append(index)  

def topoSort(adjList): 
    stack = []
    visitedArray = [0 for _ in range(len(adjList))] 

    for i in range(len(adjList)): 
        if visitedArray[i] == 0: 
            dfs(adjList, visitedArray, stack, i)
    
    return stack[::-1]