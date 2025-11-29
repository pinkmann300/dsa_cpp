class TreeNode: 
    def __init__(self, key = None, left = None, right = None):
        self.key = key 
        self.left = left 
        self.right = right 

def hashMapBuild(inorder): 
    hashMap = {val : idx for idx, val in enumerate(inorder)} 
    return hashMap 


def buildTree(preOrder, inOrder): 
    hashMap = hashMapBuild(inOrder) 

    def build(preStart, preEnd, inStart, inEnd): 
        if preStart > preEnd or inStart > inEnd: 
            return None 

        root_val = preOrder[preStart] 
        root = TreeNode(root_val) 

        rootIndex = hashMap[root_val]
        leftCount = rootIndex - inStart 

        root.left = build(preStart + 1, preStart + leftCount, inStart, rootIndex - 1) 
        root.right = build(preStart + leftCount + 1, preEnd, inStart + 1, inEnd)

        return root 

    build(0, len(preOrder) - 1, 0, len(inOrder) - 1) 

 
