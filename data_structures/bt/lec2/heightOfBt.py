from collections import deque

class BTree: 
    def __init__(self, data = None, left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def heightOfBt(tree): 
    if not tree: 
        return 0 
    left = 1 + heightOfBt(tree.left) 
    right = 1 + heightOfBt(tree.right) 
    return max(left, right) 

binTree1 = BTree(5, BTree(6, None, BTree(7, None)), BTree(6, BTree(4, BTree(5, None, None), None), None)) 
print(heightOfBt(binTree1))

def levelOrder(tree): 
    if not tree:
        return 0 
    
    q = deque()
    levelOrderArray = [] 
    q.append(tree) 
    while q: 
        size = len(q) 
        levels = [] 
        for _ in range(size): 
            node = q.popleft() 

            levels.append(node.data) 
            levelOrderArray = levelOrderArray + [levels] 

            if (node.left):
                q.append(node.left) 

            if (node.right):
                q.append(node.right) 

    return levelOrderArray 
            
        
print(levelOrder(binTree1))