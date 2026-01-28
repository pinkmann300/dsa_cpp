class DisjointSet: 
    def __init__(self, n): 
        self.rank = [0 for _ in range(n)] 
        self.parent = [i for i in range(n)] 

    def union(self, u, v):
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


    def findUltimateParent(self, u):
        if self.parent[u] == u: 
            return u 
        else: 
            currentParent = self.parent[u] 
            k = self.findUltimateParent(currentParent); 
            self.parent[u] = k  
            return k 
    


            