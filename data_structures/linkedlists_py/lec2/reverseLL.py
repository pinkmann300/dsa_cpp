class Node : 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 


def reverseLinkedList(head: Node):
    prev = None
    current = head 
    while (current is not None): 
        temp = current.next
        current.next = prev 
        prev = current
        current = temp

    return prev

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

head = reverseLinkedList(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
printLL(head)