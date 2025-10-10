class BinaryTree: 
    def __init__(self, data = None, left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def inOrder(tree, arr): 
    if tree is None: 
        return arr 
    else: 
        inOrder(tree.left, arr)  
        arr.append(tree.data) 
        inOrder(tree.right, arr) 

def inOrderStart(tree): 
    arr = [] 
    inOrder(tree, arr) 
    return arr 

def inOrderIterative(tree): 
    inOrderArray = [] 
    traversalStack = []
    if tree is None: 
        return inOrderArray 
    
    current = tree 
    while current or traversalStack:
        while current:  
            traversalStack.append(current) 
            current = current.left
        
        current = traversalStack.pop() 
        inOrderArray.append(current.data) 
        current = current.right 
    
    return inOrderArray

    
    

binaryTree = BinaryTree(3, BinaryTree(4, None, BinaryTree(5, None))) 
print(inOrderStart(binaryTree))