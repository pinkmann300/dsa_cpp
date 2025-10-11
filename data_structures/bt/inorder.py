from binary_trees import BTree
from binary_trees import binTree1

from collections import deque 

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
    

def symmetricHelper(tree1, tree2): 
    if not tree1 and not tree2: 
        return True 
    
    if not tree1 or not tree2: 
        return False 
    
    if (tree1.data == tree2.data): 
        left1 = symmetricHelper(tree1.left, tree2.right) 
        right1 = symmetricHelper(tree1.right, tree2.left) 
        return left1 and right1 
    else: 
        return False 
    

def symmetricTrees(tree): 
    tree1 = tree.left 
    tree2 = tree.right 

    return symmetricHelper(tree1, tree2)

print(inorder(binTree1))

def zigZagTraversal(tree): 
    zigZag = []
    leftToRight = True 
    queue = deque() 
    if not tree: 
        return zigZag 
    while queue: 
        size = len(queue) 
        row = [0] * size  

        for i in range(size): 
            index = i if leftToRight else (size - 1 - i) 
            node = queue.popleft() 
            row[index] = node.data 

            if node.left: 
                queue.append(node.left) 

            if node.right: 
                queue.append(node.right)

        leftToRight = not leftToRight 
        zigZag = zigZag + [row] 

    return zigZag


tree = BTree(1,
             BTree(2, BTree(3), BTree(4)),
             BTree(2, BTree(4), BTree(3)))


print(symmetricTrees(tree))