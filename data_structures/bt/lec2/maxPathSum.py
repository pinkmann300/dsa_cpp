class Node: 
    def __init__(self, key, left = None, right = None): 
        self.key = key 
        self.left = left 
        self.right = right 


def maximumPathSum(root): 
    maxSum = float('-inf') 
    def dfs(root): 
        nonlocal maxSum 
        if not root: 
            return 0 
            
        left = max(0, dfs(root.left)) 
        right = max(0, dfs(root.right)) 
        maxSum = max(maxSum, left + right + root.key)

        return (max(left, right) + root.key)

    dfs(root)
    return maxSum


def heightOfTree(root): 
    if not root: 
        return 0  
    else: 
        right = 1 + heightOfTree(root.right) 
        left = 1 + heightOfTree(root.left)

        return max(right, left) 
    

def identicalTrees(root1, root2): 
    if not root1 and not root2: 
        return True   

    if not root1 or not root2: 
        return False 
    
    if root1.key == root2.key: 
        return identicalTrees(root1.left, root2.left) and identicalTrees(root1.right, root2.right) 
    else: 
        return False 
    


def diameter(root): 
    maxDiameter = float('-inf') 
    def dfs(root): 
        nonlocal maxDiameter
        if not root: 
            return 0 
        else: 
            left = max(0, dfs(root.left)) 
            right = max(0, dfs(root.right)) 

            maxDiameter = max(left + right, maxDiameter)

            return (max(left, right) + 1)
        
    dfs(root) 
    return maxDiameter

    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)


print(diameter(root))

