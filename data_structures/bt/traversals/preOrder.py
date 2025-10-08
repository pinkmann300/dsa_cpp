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


def preOrderIterative(tree): 
    preOrderArray = [] 
    preOrderStack = [] 
    if tree is None: 
        return preOrderArray 

    preOrderStack.append(tree) 
    
    while preOrderStack: 
        node = preOrderStack.pop() 
        preOrderArray.append(node.data) 
        if (node.right): 
            preOrderStack.append(node.right) 
        
        if (node.left): 
            preOrderStack.append(node.left) 
    
    return preOrderArray
 

    


binaryTree = BinaryTree(3, BinaryTree(4, BinaryTree(6, None), BinaryTree(5, None))) 
print(preOrderIterative(binaryTree))

