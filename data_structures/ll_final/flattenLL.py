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


head = Node(5)
head.child = Node(14)
head.next = Node(10)
head.next.child = Node(4)
head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17) 


head = flattenLL(head)
printLL(head)
    

    