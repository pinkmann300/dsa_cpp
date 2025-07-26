class Node: 
    def __init__(self, val, next=None, prev=None): 
        self.val = val 
        self.next = next 
        self.prev = prev 


def deleteAllOccurences(head, key): 
    if (head is None): 
        return head 
    
    while (head.val == key): 
        head = head.next

    temp = head 

    while temp is not None: 
        if (temp.val == key): 
            prevNode = temp.prev 
            nextNode = temp.next 

            prevNode.next = nextNode
            temp = nextNode 
        else: 
            temp = temp.next 
    
    return head 






            


    
