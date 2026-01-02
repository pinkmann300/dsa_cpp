from collections import deque

def bfs(adjacencyList, V): 
    visited_array = [False for _ in range(V + 1)] 
    bfs_list = [] 

    for i in range(len(adjacencyList)): 
        if (visited_array[i]) == False: 
            visited_array[i] = True 
            que = deque() 
            que.append(i) 

            while que: 
                node = que.popleft() 
                bfs_list.append(node) 

                for nodes in adjacencyList[node]: 
                    if not visited_array[nodes]: 
                        visited_array[nodes] = True 
                        que.append(nodes) 

    return bfs_list       
