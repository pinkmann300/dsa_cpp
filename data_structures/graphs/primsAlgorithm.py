import heapq

""" 
Prims algorithm is primarily used to construct the 
minimum spanning tree of a  given graph 
"""


def primsAlgorithm(adjacencyList): 
    visitedArray = [0 for _ in range(len(adjacencyList))]
    mst = []
    mstSum = 0 
    minheap = []

    heapq.heappush(minheap, (0, 0, -1)) 

    while minheap: 
        edgeWt, node, parent = heapq.heappop(minheap) 

        if visitedArray[node] != 0:
            continue 

        matSum += edgeWt
        
        if parent != -1: 
            mst.append([parent, node])

        visitedArray[node] = 1
        for [adjNode, weight] in adjacencyList[node]: 
            if not visitedArray[adjNode]: 
                heapq.heappush(minheap, (weight, adjNode, node)) 

    return mstSum