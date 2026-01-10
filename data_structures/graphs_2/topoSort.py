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


def kahnsAlgorithm(adjList): 
    topoSortList = [] 
    queue = deque() 
    indegreeArray = [0] * len(adjList) 
    for i in range(len(adjList)): 
        for j in adjList[i]: 
            indegreeArray[j] += 1 

    for k in range(len(indegreeArray)): 
        if indegreeArray[k] == 0: 
            queue.append(k)

    while queue:
        node = queue.popleft() 
        topoSortList.append(node) 

        for k in adjList[node]: 
            indegreeArray[k] -= 1 

            if indegreeArray[k] == 0: 
                queue.append(k) 
    return topoSortList


def cycleDetection(adjList): 
    topoList = kahnsAlgorithm(adjList) 
    return False if (len(topoList) == len(adjList)) else True 