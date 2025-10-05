from binary_trees import BTree 
from binary_trees import binTree1 

def maxSumPath(tree): 
    if not tree: 
        return 0 
    else: 
        left = tree.data + maxSumPath(tree.left) 
        right = tree.data + maxSumPath(tree.right) 
        pass 

    
        return 