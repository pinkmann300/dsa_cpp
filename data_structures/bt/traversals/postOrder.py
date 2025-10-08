class BinaryTree: 
    def __init__(self, data = None, left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def postOrder(tree, arr): 
    if tree is None: 
        return 
    else:
        postOrder(tree.left, arr) 
        postOrder(tree.right, arr) 
        arr.append(tree.data)

def postOrderStart(tree): 
    arr = [] 
    postOrder(tree, arr) 
    return arr 

binaryTree = BinaryTree(3, BinaryTree(4, None, BinaryTree(5, None)))
print(postOrderStart(binaryTree))