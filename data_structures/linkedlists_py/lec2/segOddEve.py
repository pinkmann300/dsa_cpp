class Node: 
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

def segOddEven(head):
    odd = Node(-1) 
    temp0 = odd
    even = Node(-1)
    tempe = even 

    curr = head 
    while (curr != None):
        temp = curr
        curr = curr.next 
        temp.next = None;
        if (temp.data % 2 == 1):
            temp0.next = temp; 
            temp0 = temp0.next 
        else:
            tempe.next = temp
            tempe = tempe.next
    tempe.next = odd.next
    return even.next

def printLL(head: Node):
    temp = head
    while (temp != None) :
        print(temp.data, "->", end="")
        temp = temp.next


head = Node(1); 
head.next = Node(2);
head.next.next = Node(3);
head.next.next.next = Node(4);


segregated = segOddEven(head)
printLL(segregated); 

    
        
            
