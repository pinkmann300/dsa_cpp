from collections import deque

class BinaryTree: 
    def __init__(self, data = None, left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def levelOrder(tree): 
    travQueue = deque() 
    levelOrder = [] 
    travQueue.append(tree)

    while travQueue: 
        size = len(travQueue) 
        levels = [] 

        for _ in range(size):

            node = travQueue.popleft() 
            if node.left: 
                travQueue.append(node.left) 
            if node.right: 
                travQueue.append(node.right) 
            levels.append(node.data) 
        levelOrder = levelOrder + [levels] 

    return levelOrder
        

binaryTree = BinaryTree(3, BinaryTree(4, None, BinaryTree(5, None))) 
print(levelOrder(binaryTree))