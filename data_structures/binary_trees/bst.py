class BST: 
    def __init__(self, data = None,left = None, right = None): 
        self.data = data 
        self.left = left 
        self.right = right 

def searchKey(key, tree): 
    while tree: 
        if tree.data == key: 
            return True  
        
        if tree.data > key: 
            tree = tree.left 
        
        if tree.data < key: 
            tree = tree.right

    return False 


def ceil(key, tree): 
    ceilValue = -1 

    while tree: 
        if (tree.data == key): 
            ceilValue = tree.data 
            return ceilValue 
        else: 
            if (tree.data > key):
                ceilValue = tree.data 
                tree = tree.left 
            else: 
                tree = tree.right 

    return ceilValue 

    