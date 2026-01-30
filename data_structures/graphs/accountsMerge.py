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


def accountsMerge(mails): 
    mailMap = {} 
    dsu = DisjointSet(len(mails)) 

    for i in range(len(mails)): 
        mailInfo = mails[i] 

        for k in range(1, len(mailInfo)):
            if not mailInfo[k] in mailMap: 
                mailMap[mailInfo[k]] = i 
            else: 
                dsu.unionByRank(mailMap[mailInfo[k]], i) 
                mailMap[mailInfo[k]] = i  

    mergedMail = [[] for _ in range(n)]
    for mail, idx in mailMap.items():
        node = dsu.findUPar(idx)
        mergedMail[node].append(mail)

    # Step 3: Prepare final merged result
    ans = []
    for i in range(len(mails)):
        if not mergedMail[i]:
            continue

        mergedMail[i].sort()
        temp = [mails[i][0]]

        for mail in mergedMail[i]:
            temp.append(mail)

        ans.append(temp)

    # Sort final answer
    ans.sort()
    return ans


            

    


