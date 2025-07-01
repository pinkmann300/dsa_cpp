class Node: 
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

def revLL(head): 
    prev = None 
    curr = head 
    while (curr != None):
        temp = curr.next 
        curr.next = prev 
        prev = curr
        curr = temp 

    return prev 

def addOne(head):
    carry = 0 
    head = revLL(head)
    
    temp = head 

    
    while (temp and carry): 
        totalSum = temp.data + 1 + carry
        carry = totalSum // 10
        val = totalSum % 10 
        temp.data = val

    while (carry): 
        newNode = Node(carry, None)
        temp.next = N