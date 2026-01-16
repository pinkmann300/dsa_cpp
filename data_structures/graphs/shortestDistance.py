from collections import deque

def shortestDistance(adjacencyList, source): 
    distanceArray = [float('inf') for _ in range(len(adjacencyList))] 
    queue = deque() 

    queue.append((source, 0)) 
    distanceArray[source] = 0  

    while queue: 
        node, distance = queue.popleft() 
        for neighbour in adjacencyList[node]: 
            newDistance = distance + 1 
            if newDistance < distanceArray[neighbour]:
                queue.append((neighbour, newDistance))
            

    resultantArray = [0 for _ in range(len(adjacencyList))] 

    for k in range(len(distanceArray)):
        if distanceArray[k] != float('inf'): 
            resultantArray[k] = distanceArray[k] 
        else: 
            resultantArray[k] = -1 


    return resultantArray

         




    