from collections import deque

class TreeNode: 
    def __init__(self, key = None, left = None, right = None): 
        self.key = key 
        self.left = left 
        self.right = right 


def serialiseTree(root): 
    queue = deque() 
    serString = "" 

    if not root: 
        return serString 
    
    queue.append(root) 

    while queue: 
        node = queue.popleft() 

        if node is None: 
            serString += "#,"

        else:
            serString += str(node.key) + ","
            queue.append(node.left) 
            queue.append(node.right) 

    return serString


def deserialiseTree(serialisedString): 
    if serialisedString == "":
        return None 
    
    nodeVals = serialisedString.split(",") 

    root = TreeNode(nodeVals[0]) 
    queue = deque() 
    queue.append(root) 

    i = 1 

    while queue and i < len(nodeVals) - 1: 
        current = queue.popleft() 
        
        if nodeVals[i] != "#": 
            left = TreeNode(nodeVals[i]) 
            current.left = left
            queue.append(left) 

        i += 1 

        if nodeVals[i] != "#": 
            right = TreeNode(nodeVals[i])
            current.right = right 
            queue.append(right) 

        i += 1 

    return root 




    pass



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
 

print(serialiseTree(root)) 



                

