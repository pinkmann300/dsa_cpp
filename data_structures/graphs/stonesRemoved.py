class DisjointSet: 
    def __init__(self, n): 
        self.rank = [0 for _ in range(n)] 
        self.parent = [i for i in range(n)] 

    def findUltimateParent(self, u): 
        if self.parent[u] == u: 
            return u 
        else: 
            currentParent = self.parent[u] 
            k = self.findUltimateParent(currentParent) 
            self.parent[u] = k
            return self.parent[u] 

    def unionByRank(self, u, v): 
        pu = self.findUltimateParent(u) 
        pv = self.findUltimateParent(v) 

        if pu == pv: 
            return 
    
        if self.rank[pu] == self.rank[pv]: 
            self.rank[pu] += 1 
            self.parent[pv] = pu 
        
        elif self.rank[pu] > self.rank[pv]: 
            self.parent[pv] = pu 

        else: 
            self.parent[pu] = pv 


def mostStonesRemoved(stoneCoords): 
    maxRow = 0 
    maxCol = 0 

    for x, y in stoneCoords: 
        maxRow = max(maxRow, x) 
        maxCol = max(maxCol, y) 

    dsuSize = maxRow + maxCol + 1 
    dsu = DisjointSet(dsuSize) 
    componentsSet = set()

    for x, y in stoneCoords: 
        row = x 
        col = y + maxRow + 1 

        if dsu.findUltimateParent(row) != dsu.findUltimateParent(col):
            dsu.unionByRank(row, col) 
        
    
    totalNumberOfStones = len(stoneCoords) 
     
    for x, y in stoneCoords: 
        row = x 
        col = y + maxRow + 1 

        componentsSet.add(dsu.findUltimateParent(row)) 
        componentsSet.add(dsu.findUltimateParent(col))

    numberOfComponents = len(componentsSet) 

    maxStonesRemoved = totalNumberOfStones - numberOfComponents 

    return maxStonesRemoved
        

    




