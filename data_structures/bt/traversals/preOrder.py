class BinaryTree: 
    def __init__(self, data = None, left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def preOrder(tree, arr): 
    if tree is None: 
        return 
    else: 
        arr.append(tree.data) 
        preOrder(tree.left, arr) 
        preOrder(tree.right, arr) 

def preOrderStart(tree): 
    arr = [] 
    preOrder(tree, arr) 
    return arr 


binaryTree = BinaryTree(3, BinaryTree(4, None, BinaryTree(5, None))) 
print(preOrderStart(binaryTree))

