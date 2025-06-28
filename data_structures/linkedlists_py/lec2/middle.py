class Node: 
    def __init__(self, data, next= None): 
        self.data = data 
        self.next = next


def middleOfll(head: Node) : 
    slow: Node = head
    fast: Node = head

    while (fast != None and fast.next != None) :
        fast = fast.next.next
        slow = slow.next

    return slow.data

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle node
middle_node = middleOfll(head)

# Display the value of the middle node
print("The middle node value is:", middle_node)