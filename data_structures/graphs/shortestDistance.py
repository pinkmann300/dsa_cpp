from collections import

def shortestDistance(adjacencyList): 
    distanceArray = [float('inf') for _ in range(len(adjacencyList))] 
    queue = deque() 