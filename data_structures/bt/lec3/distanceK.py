from collections import deque

class TreeNode: 
    def __init__(self, key = None, left = None, right = None): 
        self.key = key 
        self.left = left 
        self.right = right 


def create_parent_map(root): 
    parent_map = {} 

    if not root: 
        return parent_map 
    
    queue = deque()
    queue.append(root) 

    while queue:
        node = queue.popleft() 

        if node.left: 
            parent_map[node.left] = node 
            queue.append(node.left) 
        
        if node.right: 
            parent_map[node.right] = node 
            queue.append(node.right) 

    return parent_map 

def atDistanceK(root, target, k): 
    parent_map = create_parent_map(root) 

    queue = deque()
    visited = set() 

    level = 0 
    queue.append(target) 
    visited.add(target) 


    while queue:

        if level == k:
            break 

        level_size = len(queue) 

        for _ in range(0, level_size): 
            node = queue.popleft()

            if node.left and not node.left in visited: 
                visited.add(node.left) 
                queue.append(node.left) 

            if node.right and not node.right in visited: 
                visited.add(node.right) 
                queue.append(node.right) 

            if node in parent_map and not parent_map[node] in visited:
                visited.add(parent_map[node]) 
                queue.append(parent_map[node]) 

        level += 1 

    return [q.key for q in queue]


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


target = root.left  # Node with value 5
k = 2

finalList = atDistanceK(root, target, k) 
print(finalList)    