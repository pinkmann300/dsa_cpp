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

print(inorder(binTree1))