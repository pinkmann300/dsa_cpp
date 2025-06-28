class Node: 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 

def printLL(head: Node): 
    temp = head
    while (temp != None): 
        print(temp.data, "->", end="")
        temp = temp.next 

def recursiveRec(head: Node, target: Node):
    if (head == None): 
        return target
    else: 
        newNode = Node(head.data, target)
        head = head.next
        return recursiveRec(head, newNode); 

def reverse(head):
    return recursiveRec(head, None); 

def printLL(head: Node):
    temp = head
    while (temp != None) :
        print(temp.data, "->", end="")
        temp = temp.next


head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:",)
printLL(head)

print("\n")

head = reverse(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
printLL(head)
