class TreeNode: 
    def __init__(self, key = None, left = None, right = None):
        self.key = key 
        self.left = left 
        self.right = right 


def countNodes(root): 
    if not root: 
        return 0 
    
    lh = findLeftHeight(root) 
    rh = findRightHeight(root) 

    if lh == rh: 
        return (2 ** lh) - 1 
    
    return 1 + countNodes(root.left) + countNodes(root.right) 


def findLeftHeight(root): 
    height = 0 
    while root: 
        height += 1 
        root = root.left 
    return height 


def findRightHeight(root): 
    height = 0 
    while root: 
        height += 1 
        root = root.right 
    return height 


if __name__ == "__main__":
    # Create binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    # Create solution object


    # Count total nodes
    totalNodes = countNodes(root)

    # Output result
    print("Total number of nodes in the Complete Binary Tree:", totalNodes)
