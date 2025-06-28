class ListNode: 
    def __init__(self, data, next): 
        self.data = data 
        self.next = next

    def printList(self): 
        tempNode : ListNode = self
        while (tempNode is not None): 
            print(tempNode.data, "-->", end=" ")
            tempNode = tempNode.next



# Main Program begins here. 
x = ListNode(2, ListNode(4, None))
x.printList()
    