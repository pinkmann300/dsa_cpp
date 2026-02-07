from collections import deque 

def cycleDetection(adjList, srcNode, visited): 
    if not adjList: 
        return False 
    
    queue = deque() 
    queue.append((srcNode, -1)) 
    visited[srcNode] = True 

    while queue: 
        node, parentNode = queue.popleft() 
        adjacentNodes = adjList[node] 

        for i in adjacentNodes: 
            if not visited[i]: 
                queue.append((i, node)) 
            elif parentNode != i: 
                return True 
            
    return False
