class Node: 
    def __init__(self, key, left = None, right = None):
        self.key = key 
        self.left = left 
        self.right = right 


def preOrderTraversal(tree, arr):
    if (tree is None):
        return
    else: 
        arr.append(tree.key)
        preOrderTraversal(tree.left, arr) 
        preOrderTraversal(tree.right, arr) 


def preOrder(tree): 
    arr = [] 
    preOrderTraversal(tree, arr) 
    return arr


def inOrderTraversal(tree, arr): 
    if (tree is None): 
        return 
    else: 
        inOrderTraversal(tree.left, arr) 
        arr.append(tree.key) 
        inOrderTraversal(tree.right, arr) 

def postOrderTraversal(tree, arr): 
    if (tree is None): 
        return 
    else: 
        postOrderTraversal(tree.left, arr) 
        postOrderTraversal(tree.right, arr) 
        arr.append(tree.key)  

def postOrder(tree): 
    arr = []
    postOrderTraversal(tree, arr) 
    return arr  


def inOrder(tree): 
    arr = [] 
    inOrderTraversal(tree, arr) 
    return arr
        

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting preorder traversal
    result = postOrder(root)
    print(result)

    # Displaying the preorder traversal result
    print("Inorder Traversal:", end=" ")
    # Output each value in the
    # preorder traversal result
    for val in result:
        print(val, end=" ")
    print()