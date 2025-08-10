class Node: 
    def __init__(self, data, next = None): 
        self.data = data 
        self.next = next


def findMiddle(head):

    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeTwoSortedLists(left,right): 
    tempNode = Node(-1) 
    temp = tempNode

    while (left is not None and right is not None): 
        if (left.data <= right.data): 
            temp.next = left 
            left = left.next
        else: 
            temp.next = right 
            right = right.next 

        temp = temp.next 

    if (left is not None): 
        temp.next = left 
    
    if (right is not None): 
        temp.next = right

    return tempNode.next    


def sortedLinkedList(head):

    if (head is None or head.next is None): 
        return head; 


    middleNode = findMiddle(head) 

    right = middleNode.next 
    middleNode.next = None
    left = head 

    left = sortedLinkedList(left)
    right = sortedLinkedList(right) 
    return mergeTwoSortedLists(left, right)


def printLinkedList(head): 
    while head is not None: 
        print(head.data, " -> ", end="") 
        head = head.next 




head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print("Original Linked List: ", end="")
printLinkedList(head)

# Sort the linked list
head = sortedLinkedList(head)

print("Sorted Linked List: ", end="")
printLinkedList(head)
    

    