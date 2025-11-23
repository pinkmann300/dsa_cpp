from collections import deque

def bfs(V, adj):
    visited_array = [0] * (V + 1) 
    bfsArray = [] 
    visited_array[0] = 1 

    queue = deque() 
    queue.append(0) 
    
    while queue: 
        node = queue.popleft() 
        bfsArray.append(node) 
        for k in adj[node]: 
            if not visited_array[k]: 
                visited_array[k] = 1 
                queue.append(k) 

    return bfsArray

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def printAns(ans):
    for x in ans:
        print(x, end=" ")


if __name__ == "__main__":
    adj = [[] for _ in range(6)]    
    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)