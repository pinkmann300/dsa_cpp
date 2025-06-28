class Node: 
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

def rotateLL(head, k):
    # Making it a circular linked list. 

    temp = head; 
    while (temp.next != None): 
        temp = temp.next 

    temp.next = head; 
    # Connects the last node to the head node. 
    delLink = head

    for i in range(k): 
        delLink = delLink.next
    
    newHead = delLink.next
    delLink.next = None
    
    return newHead
        
 
def printLL(head): 
    while (head != None): 
        print(head.data, "->", end="")
        head = head.next 


# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head

if __name__ == '__main__':
    head = None
    # inserting Node
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printLL(head)


    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rotateLL(head, k)

    print("\n"); 

    print("After", k, "iterations: ", end='')
    printLL(newHead)
