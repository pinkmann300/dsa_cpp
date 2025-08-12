class Node: 
    def __init__(self, data, next = None, random = None): 
        self.data = data 
        self.next = next 
        self.random = random

def insertCopyInBetween(head): 
    temp = head 
    while temp is not None: 
        copyNode = Node(temp.data) 
        copyNode.next = temp.next 
        temp.next = copyNode 

        temp = temp.next.next 

    return head 

def makeRandomConnections(head): 
    temp = head 
    while (temp is not None): 
        randomNode = temp.random 
        temp.next.random = randomNode.next if randomNode is not None else None 

        temp = temp.next.next 

    return head 

def getDeepCopyList(head):
    temp = head
    dummyNode = Node(-1)

    res = dummyNode

    while temp:
        res.next = temp.next
        res = res.next

        temp.next = temp.next.next
        temp = temp.next

    return dummyNode.next



def printLL(head): 
    while (head is not None): 
        print(head.data, " -> ", end= "")
        head = head.next 


head = Node(7)
head.next = Node(14)
head.next.next = Node(21)
head.next.next.next = Node(28)

head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next
head.next.next.next.random = head.next

head = getDeepCopyList(makeRandomConnections(insertCopyInBetween(head)))

printLL(head)
