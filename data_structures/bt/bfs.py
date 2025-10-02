from collections import deque

class Tree: 
    def __init__(self, data = None, left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def bfs(tree): 
    ans = []
    if tree is None: 
        return ans 
    
    q = deque() 
    q.append(tree) 
    
    while q: 
        levels = []
        size = len(q) 
        for _ in range(size):
            node = q.popleft() 
            levels.append(node.data) 

            if node.left is not None:
                q.append(node.left) 

            if node.right is not None: 
                q.append(node.right) 
    
        ans.append(levels) 

    return ans 
            


binTree1 = Tree(5, Tree(6, None, Tree(7, None)), None) 
print(bfs(binTree1))
    