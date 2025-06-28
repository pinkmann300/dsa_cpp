class ListNode: 
    def __init__(self, data, next): 
        self.data = data 
        self.next = next

    def printList(self): 
        tempNode : ListNode = self
        while (tempNode is not None): 
            print(tempNode.data,"->", end=" ")
            tempNode = tempNode.next


def insertAtHead(node1, val): 
    tempNode : ListNode = ListNode(val, None); 
    tempNode.next = node1; 
    return tempNode;  


def insertAtTail(node1, val):
    tempNode: ListNode = node1; 
    while (tempNode.next != None):
        tempNode = tempNode.next; 
    tempNode.next = ListNode(val, None); 
    return node1


def deleteNode(node1): 
    if ((node1 == None) or (node1.next == None)): 
        return None
    
    tempNode : ListNode = node1
    while (tempNode.next.next != None): 
        tempNode = tempNode.next; 

    tempNode.next = None; 
    return node1


def lengthOfll(node1 : ListNode):
    tempNode = node1 
    count = 0
    while (tempNode != None): 
        count += 1
        tempNode = tempNode.next
    
    return count


def searchElement(node1: ListNode, val) : 
    tempNode: ListNode = node1
    while (tempNode != None):
        if (tempNode.data == val):
            return True
        tempNode = tempNode.next
    return False

def deleteHead(node1: ListNode) :
    if ((node1 == None) or (node1.next == None)): 
        return None; 
    
    tempNode = node1
    return tempNode.next



    



# Main Program begins here. 
x = ListNode(2, ListNode(4, None))
x = insertAtHead(x, 4); 
x = insertAtTail(x, 6); 
x = deleteNode(x); 
x = deleteHead(x); 
print(searchElement(x, 7))
print(searchElement(x, 4))
x.printList(); 

