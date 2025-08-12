class Node: 
    def __init__(self, data, next = None, child = None): 
        self.data = data 
        self.next = next 
        self.child = child 

def flattenLL(head): 
    newList = [] 
    temp = head 
    while (temp is not None): 
        temp2 = temp
        while (temp2 is not None): 
            newList.append(temp2.data)
            temp2 = temp2.child 
        temp = temp.next 

    newList.sort() 
    dummyNode = Node(-1, None, None) 
    temp3 = dummyNode
    for i in range(len(newList)): 
        temp3.child = Node(newList[i], None, None)
        temp3 = temp3.child 
    
    return dummyNode.child  

def printLL(head): 
    while head is not None: 
        print(head.data, " -> ", end="")
        head = head.child 

def merge2Heads(left, right):
    dummyNode = Node(-1)
    temp = dummyNode 

    while (left is not None and right is not None): 
        if (left.data <= right.data):
            temp.child = left 
            left = left.child
        else: 
            temp.child = right
            right = right.child 

        temp = temp.child

    if (left is not None): 
        temp.child = left 

    if (right is not None): 
        temp.child = right

    temp.next = None
    

    return dummyNode.child 

def flattenLinkedList(head):
    if not head or not head.next:
        return head

    mergedHead = flattenLinkedList(head.next)
    head = merge2Heads(head, mergedHead)
    return head

def flattenLinkedList2(head):
    temp = head 
    mergedHead = temp

    while (temp is not None and temp.next is not None):
        mergedHead = merge2Heads(mergedHead, temp.next) 
        temp = temp.next  
    
    return mergedHead


head = Node(5)
head.child = Node(14)
head.next = Node(4)
head.next.child = Node(10)
head.next.next = Node(9)
head.next.next.child = Node(13)
head.next.next.child.child = Node(20)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17) 


printLL(flattenLinkedList2(head))