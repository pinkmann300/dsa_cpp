from collections import deque


""" 
The code below describes the Dijkstra's algorithm for finding the shortest distance 
from a source node to any other node in the graph given. Dijkstra's algorithm is very 
similar to the BFS algorithm. 

Initial configuration for the algorithm. 

    1) Distance array : An array of size len(graph) where each element stores an 
    extremely high value. For example float('inf'). 

    2) A priority queue: A min heap data structure which will replace the queue 
    data structure that we have traditionally been using for the BFS traversals. 

    3) A source node: The node from which we will start the Dijkstra algorithm to find 
    the shortest distance to other nodes. dist[sourceNode] = 0 as the distance from a 
    node to itself in the shortest configuration would be 0. 
"""

import heapq 


def dijkstras(adjList, sourceNode): 
    distanceArray = [float('inf') for _ in range(len(adjList))] 
    minheap = [] 

    distanceArray[sourceNode] = 0 
    heapq.heappush(minheap, (0, sourceNode))  

    while minheap: 
        distance, node = heapq.heappop(minheap) 

        for neighbour, neighbourDist in adjList[node]: 
            if distanceArray[neighbour] > (neighbourDist + distance): 
                heapq.heappush(minheap, (neighbourDist + distance, neighbour))
                distanceArray[neighbour] = neighbourDist + distance

    return distanceArray

"""
Why do we use a priority queue instead of a queue? 

Since, we use a min-heap, we will only work initially with the shortest routes 
to a particular node and any other paths can be disconsidered going forward because we 
try and work with a slightly greedy approach in some sense. You will end up exploring 
too many paths unnecessarily. 


Why is the time complexity E log V  (E is the total number of edges and V is the number of 
vertices) ?

The while loop in a priority queue would run for a time complexity of log V. 


"""

def networkDelayTime( times, n, k):
        adjacencyList = [[] for _ in range(n + 1)] 
        for [start, target, weight] in times: 
            adjacencyList[start].append((target, weight)) 

        timeArray = [float('inf') for _ in range(n + 1)]
        travque = deque() 

        travque.append((k, 0))
        timeArray[k] = 0 

        while travque: 
            point, time = travque.popleft()

            for nextPoint, travelTime in adjacencyList[point]:
                newTime = time + travelTime 

                if newTime < timeArray[nextPoint]:
                    timeArray[nextPoint] = newTime 
                    travque.append((nextPoint, newTime)) 

        
        return -1 if max(timeArray[1:]) == float('inf') else max(timeArray[1:]) 
