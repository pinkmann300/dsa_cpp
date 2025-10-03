from binary_trees import BTree 

def preorder(tree): 
    stack = [] 
    preorder_array = [] 

    if tree is None: 
        return preorder_array 
    
    stack.append(tree)

    while stack: 
        node = stack.pop() 
        preorder_array.append(node.data) 

        if node.right is not None: 
            stack.append(node.right) 
        if node.left is not None: 
            stack.append(node.left) 

    return preorder_array

binTree1 = BTree(5, BTree(6, None, BTree(7, None)), BTree(8, None)) 
print(preorder(binTree1))
 



        
