class Node: 
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 


def findMiddle(head: Node):
    slow = head 
    fast = head 

    while (fast != None and fast.next != None):
        slow = slow.next 
        fast = fast.next.next 

    return slow


def sortLL(head):
    if ((head == None) or (head.next == None)):
        return head 
    
    middle = findMiddle(head); 
    right = middle.next 
    middle.next = None 
    left = head 

    left = sortLL(left)
    right = sortLL(right)

    return mergeTwoLists(left, right)


def mergeTwoLists(left, right):
    dummyNode = Node(-1)
    temp = dummyNode

    # Traverse both lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare elements of both lists and
        # link the smaller node to the merged list
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        # Move the temporary pointer
        # to the next node
        temp = temp.next 

    # If any list still has remaining
    # elements, append them to the merged list
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    
    # Return the merged list starting 
    # from the next of the dummy node
    return dummyNode.next
    
