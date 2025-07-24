class DNode: 
    def __init__(self, val, next=None, prev=None): 
        self.val = val 
        self.next = next
        self.prev = prev

def printDLL(head):
    while head is not None: 
        print(head.val, "<->", end=" ")
        head = head.next 

def insertAtEnd(head, k):
    newNode = DNode(k, None, None)

    if head is None: 
        return DNode(k, None, None) 
    
    temp = head
    while temp.next is not None: 
        temp = temp.next 

    temp.next = newNode
    newNode.prev = temp 
    
    return head 

def deleteNode(head): 
    # Deleting the tail of a linked list. 
    if head is None or head.next is None: 
        return None 
    
    temp = head 
    while temp.next is not None: 
        temp = temp.next 
    
    previousNode = temp.prev 
    previousNode.next = None 

    temp.prev = None
    del temp 

    return head 

def reverseDLL(head): 
    if head is None or head.next is None: 
        return head 
    
    prev = None 
    current = head 
    while current is not None: 
        prev = current.prev  
        current.prev = current.next 
        current.next = prev 
        current = current.prev 
    return prev.prev 

def convert_arr_to_dll(arr):
    # Create the head node with
    # the first element of the array
    head = DNode(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the
        # array and set its 'back' pointer
        # to the previous node
        temp = DNode(arr[i], None, prev)
        
        # Update the 'next' pointer of the
        # previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created 
        # node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head



# Example usage:
arr = [12, 5, 6, 8, 4]
# Convert the array to a
# doubly linked list
head = convert_arr_to_dll(arr)
# Print the doubly linked list
print('Doubly Linked List Initially:  ')
printDLL(head)

print('Doubly Linked List After Reversing :')

# Reverse the doubly linked list
head = reverseDLL(head)
# Print the reversed doubly linked list
printDLL(head)


    