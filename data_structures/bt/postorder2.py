from binary_trees import BTree 
from binary_trees import binTree1

def postOrder2(tree):
    post_stack = []
    traversal_stack = []

    traversal_stack.append(tree) 

    while traversal_stack: 
        node = traversal_stack.pop() 
        if node.left: 
            traversal_stack.append(node.left) 
        if node.right: 
            traversal_stack.append(node.right) 

        post_stack.append(node.data) 

    post_stack.reverse() 

    return post_stack

print(postOrder2(binTree1))
