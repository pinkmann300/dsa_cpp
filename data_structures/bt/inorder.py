from binary_trees import BTree
from binary_trees import binTree1


def inorder(tree): 
    current = tree 
    stack = [] 
    results = []
    while current or stack: 
        while current: 
            stack.append(current) 
            current = current.left 

        current = stack.pop() 
        results.append(current.data) 
        current = current.right 

    return results 

def identicalTrees(tree1, tree2): 

    if tree1 and not tree2: 
        return False 
    
    if tree2 and not tree1: 
        return False 

    if not tree1 and not tree2:
        return True 
    
    if (tree1.data == tree2.data):
        left1 = identicalTrees(tree1.left, tree2.left) 
        right1 = identicalTrees(tree1.right, tree2.right) 
        return left1 and right1
    else:
        return False 
    
    



print(inorder(binTree1))

