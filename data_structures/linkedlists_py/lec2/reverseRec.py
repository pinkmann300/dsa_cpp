class Node: 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 


def printLL(head: Node): 
    temp = head
    while (temp != None): 
        print(temp.data, "->", end="")
        temp = temp.next 


def recursiveRec(head: Node, target: Node):
    if (head == None): 
        return target
    else: 
        newNode = Node(head.data, target)
        head = head.next
        return recursiveRec(head, newNode); 


def reverse(head):
    return recursiveRec(head, None); 


def printLL(head: Node):
    temp = head
    while (temp != None) :
        print(temp.data, "->", end="")
        temp = temp.next


def reverse_linked_list(head):
    # Base case:
    # If the linked list is empty or has only one node,
    # return the head as it is already reversed.
    if head is None or head.next is None:
        return head
    
    # Recursive step:
    # Reverse the linked list starting from the second node (head.next).
    new_head = reverse_linked_list(head.next)



    # Save a reference to the node following
    # the current 'head' node.
    front = head.next

    # Make the 'front' node point to the current
    # 'head' node in the reversed order.
    front.next = head

    # Break the link from the current 'head' node
    # to the 'front' node to avoid cycles.
    head.next = None
    
    # Return the 'new_head,' which is the new
    # head of the reversed linked list.
    return new_head

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked listhead = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
printLL(head)
