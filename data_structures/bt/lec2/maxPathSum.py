class TreeNode: 
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



root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(maximumPathSum(root))

