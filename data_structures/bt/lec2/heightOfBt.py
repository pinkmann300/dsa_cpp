from collections import deque

class BTree: 
    def __init__(self, data = None, left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def heightOfBt(tree): 
    if not tree: 
        return 0 
    left = 1 + heightOfBt(tree.left) 
    right = 1 + heightOfBt(tree.right) 
    return max(left, right) 

def levelOrder(tree): 
    if not tree:
        return 0 
    
    q = deque()
    levelOrderArray = [] 
    q.append(tree) 
    while q: 
        size = len(q) 
        levels = [] 
        for _ in range(size): 
            node = q.popleft() 

            levels.append(node.data) 
            levelOrderArray = levelOrderArray + [levels] 

            if (node.left):
                q.append(node.left) 

            if (node.right):
                q.append(node.right) 

    return levelOrderArray 
            
def maximumWidth(tree): 
    if not tree: 
        return 0  
    maxWidth = 0 
    q = deque() 
    q.append((tree,1)) 
    while q: 
        size = len(q) 
        levels = [] 
        for _ in range(size): 
            node, parentIndex = q.popleft() 
            
            if node.left: 
                q.append((node.left, 2 * parentIndex)) 
            
            if node.right: 
                q.append((node.left, (2 * parentIndex) + 1))

            levels.append(parentIndex) 
            maxWidth = max (maxWidth,  max(levels) - min(levels) + 1)

    return maxWidth

def insertIntoBTree(root, target): 
    current = root
    while True: 
        if current.val > target: 
            if current.left: 
                current = current.left 
            else: 
                current.left = BTree(target)
                break 

        else: 
            if current.right: 
                current = current.right 
            else: 
                current.right = BTree(target) 
                break
    return root  

root = BTree(1)
root.left = BTree(3)
root.right = BTree(2)
root.left.left = BTree(5)
root.left.right = BTree(3)
root.right.right = BTree(9)

# Create object
# Print the result
print("Maximum width:", maximumWidth(root))
binTree1 = BTree(5, BTree(6, None, BTree(7, None)), BTree(6, BTree(4, BTree(5, None, None), None), None)) 
print(heightOfBt(binTree1))


haystak = "a" 

print(haystak[0:1]) 
