from binary_trees import BTree 
from collections import deque
from binary_trees import binTree1

def height1(tree): 
    height = 0 

    if tree is None: 
        return height 
    
   

    q = deque()
    q.append(tree)
    while q: 
        size = len(q) 
        for _ in range(size): 
            node = q.popleft()

            if node.left is not None: 
                q.append(node.left) 
            
            if node.right is not None: 
                q.append(node.right) 

        height += 1 

    return height 


binTree1 = BTree(5, BTree(6, None, BTree(7, None)), None) 
print(height1(binTree1))
