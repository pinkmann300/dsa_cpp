class BTree: 
    def __init__(self,data= 0,left=None, right=None): 
        self.data = data 
        self.left = left 
        self.right = right 

binTree1 = BTree(5, BTree(6, None, BTree(7, None)), None) 

#       5
#   6        7
#N      N N      N 

def heightOfTree(root): 
    if root is None: 
        return 0 
    else: 
        left = 0 
        right = 0 
        left = 1 + heightOfTree(root.left)
        right = 1 + heightOfTree(root.right) 
        return max(left, right) 

def preOrder(tree, arr): 
    if tree is None: 
        return
    else: 
        arr.append(tree.data) 
        preOrder(tree.left, arr) 
        preOrder(tree.right, arr) 

def postOrder(tree,arr): 
    if tree is None: 
        return 
    else: 
        postOrder(tree.left, arr) 
        postOrder(tree.right, arr) 
        arr.append(tree.data) 

def inOrder(tree, arr): 
    if tree is None: 
        return  
    else: 
        inOrder(tree.left, arr) 
        arr.append(tree.data) 
        inOrder(tree.right, arr) 

def traversalStart(tree): 
    arr = [] 
    postOrder(tree, arr)
    return arr  




