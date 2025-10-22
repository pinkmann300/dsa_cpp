from binary_trees import BTree
from binary_trees import binTree1
from collections import deque 
from collections import defaultdict

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


def verticalOrderTraversal(tree): 
    nodes = {}
    queue = deque() 

    vertOrder = [] 
    if not tree: 
        return vertOrder

    queue.append((tree, (0, 0))) 

    while queue: 
        node, (x, y) = queue.popleft() 
        if x in nodes:
            if y in nodes[x]:
                nodes[x][y].append(node.data) 
            else:
                nodes[x][y] = [] 
                nodes[x][y].append(node.data) 

        else:
            nodes[x] = {} 
            nodes[x][y] = []
            nodes[x][y].append(node.data)

        if (node.left): 
            queue.append((node.left, (x - 1, y + 1))) 

        if (node.right): 
            queue.append((node.right, (x + 1, y + 1))) 
    return nodes


def topViewOfTree(tree): 
    nodes = {} 
    queue = deque() 
    topView = []

    if not tree:
        return topView 

    queue.append((tree, 0)) 

    while queue: 
        node, x = queue.popleft()

        if x not in nodes: 
            nodes[x] = node.data 

        if node.left: 
            queue.append((node.left, (x - 1)))

        if node.right:
            queue.append((node.right, (x + 1))) 

    for k in (sorted(nodes.keys())): 
        topView.append(nodes[k])

    return topView


def bottomView(tree): 
    nodes = {} 
    queue = deque() 

    bottomView = [] 

    if not tree: 
        return bottomView 
    
    queue.append((tree, 0)) 

    while queue: 
        node, x = queue.popleft() 

        nodes[x] = node.data

        if node.left: 
            queue.append((node.left, (x - 1))) 
        
        if node.right: 
            queue.append((node.right, (x + 1))) 

    
    for k in (sorted(nodes.keys())): 
        bottomView.append(nodes[k]) 
    
    return bottomView


def leftView(tree): 
    nodes = {} 
    leftView = [] 
    traversalStack = []

    if not tree: 
        return leftView 
    
    traversalStack.append((tree, 0))     

    while traversalStack:
        node, y = traversalStack.pop() 
        if (node.right): 
            traversalStack.append((node.right, y + 1))
        if (node.left): 
            traversalStack.append((node.left, y + 1)) 

        if y not in nodes: 
            nodes[y] = node.data  

    print(nodes)

    for k in sorted(nodes.keys()): 
        leftView.append(nodes[k]) 

    return leftView


def rightView(tree): 
    nodes = {} 
    rightView = [] 
    traversalStack = [] 

    if not tree: 
        return rightView 
    
    traversalStack.append((tree, 0)) 

    while traversalStack: 
        node, y = traversalStack.pop() 
        if node.left: 
            traversalStack.append((node.left, y + 1)) 
        
        if node.right: 
            traversalStack.append((node.right, y + 1)) 

        if y not in nodes: 
            nodes[y] = node.data 

    for k in sorted(nodes.keys()): 
        rightView.append(nodes[k]) 

    return rightView


def isLeaf(tree): 
    return (not tree.left) and (not tree.right)

def leftBoundary(tree): 
    leftBound = [] 

    if tree is None: 
        return leftBound 
    
    current = tree 
    while current: 
        if not isLeaf(current):
            leftBound.append(current.data) 

        if current.left: 
            current = current.left  
        else: 
            current = current.right 

    return leftBound


def rightBoundary(tree): 
    rightBound = []
    if tree is None: 
        return rightBound 
    
    current = tree 

    while current: 
        if not isLeaf(current): 
            rightBound.append(current.data)

        if current.right: 
            current = current.right 
        else: 
            current = current.left 

    return rightBound


def bottomOrderRec(tree, rec): 
    if not tree: 
        return
    else: 
        if isLeaf(tree): 
            rec.append(tree.data) 
        bottomOrderRec(tree.left, rec) 
        bottomOrderRec(tree.right, rec)
            

def bottomOrder(tree): 
    arr = [] 
    bottomOrderRec(tree, arr); 
    return arr

tree = BTree(1,
             BTree(2, BTree(3), BTree(4)),
             BTree(3, BTree(4), BTree(3)))

print(bottomOrder(tree))