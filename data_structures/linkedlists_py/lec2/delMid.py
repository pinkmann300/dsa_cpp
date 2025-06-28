class Node: 
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 


def deleteMiddleNode(head): 
    if (head == None or head.next == None):
        return None
    
    slow = head
    fast = head
    fast = fast.next.next 

    while (fast != None and fast.next != None): 
        slow = slow.next 
        fast = fast.next.next 

    slow.next = slow.next.next 
    return head 

def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Creating a sample linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Display the original linked list
print("Original Linked List: ", end="")
print_linked_list(head)

# Deleting the middle node
head = deleteMiddleNode(head)

# Displaying the updated linked list
print("Updated Linked List: ", end="")
print_linked_list(head)
