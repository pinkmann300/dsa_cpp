"""
Given n nodes and a list of undirected edges. Return the number of connected components 
"""
from collections import deque
import heapq

class DisjointSet:
    def __init__(self, n): 
        self.rank = [0 for _ in range(n)]
        self.parent = [i for i in range(n)] 

    def findUltimateParent(self, u): 
        if self.parent[u] == u: 
            return u 
        else: 
            currentParent = self.parent[u] 
            k = self.findUltimateParent[currentParent] 
            self.parent[u] = k  
            return self.parent[u] 
        
    def unionByRank(self, u, v): 
        pu = self.findUltimateParent(u) 
        pv = self.findUltimateParent(v) 

        if pu == pv: 
            return 
        
        else: 
            if self.rank[pu] == self.rank[pv]: 
                self.rank[pu] += 1 
                self.parent[pv] = pu 

            elif self.rank[pu] > self.rank[pv]: 
                self.parent[pv] = pu 

            else: 
                self.parent[pu] = pv 


"""
Edges : [[0,1], [2,3] , [3,2]]
Undirected graph  
Number of nodes = n 
"""

def findNumberOfComponents(numberOfNodes, edges): 
    dsu = DisjointSet(numberOfNodes)
    components = set() 

    for [src, dst] in edges: 
        dsu.unionByRank(src, dst) 
        dsu.unionByRank(dst, src) 

    for k in range(numberOfNodes): 
        components.add(dsu.findUltimateParent(k)) 
    
    return len(components) 


def rottenOranges(grid): 
    rottenQueue = deque() 
    totalOranges = 0 
    rottenOranges = 0 

    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if grid[i][j] != 0: 
                totalOranges += 1 
                if grid[i][j] == 2: 
                    rottenQueue.append((i, j)) 

    directionVector = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    timeTaken = 0 

    while rottenQueue: 
        rottenOranges += len(rottenQueue)
        for i in range(len(rottenQueue)): 
            x, y = rottenQueue.popleft() 

            for dx, dy in directionVector: 
                nx = x + dx 
                ny = y + dy 

                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == 1: 
                    grid[nx][ny] = 2 
                    rottenQueue.append((nx, ny))
                 
        if rottenQueue: 
            timeTaken += 1

    return timeTaken if rottenOranges == totalOranges else -1


""" 
Given a list of travel times between nodes as directed weighted edges how long would it take to reach all nodes?
k = initial signal vertex 
edges = [[u, v, w], ...] 
[[0,1,2]]
"""

def signalReachTime(grid, k): 
    timeArray = [float('inf') for _ in range(len(grid))] 
    minheap = [] 
    timeArray[k] = 0 

    heapq.heappush(minheap, (0, k)) 

    while minheap: 
        time, source = heapq.heappop(minheap)
        for adjNode in grid[source]: 
            if (adjNode[1] + time) < timeArray[adjNode]: 
                timeArray[adjNode] = adjNode[1] + time
                heapq.heappush(minheap, (adjNode[1] + time, adjNode)) 

    return timeArray

    
            
    

    



                


    

        


