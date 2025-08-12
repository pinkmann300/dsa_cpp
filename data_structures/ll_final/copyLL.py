class Node: 
    def __init__(self, data, next = None, random = None ): 
        self.data = data 
        self.next = None 
        self.random = None

def createCopy(head): 
    map1 = {} 
    temp = head 
    while temp is not None: 
        newNode = Node(temp.data) 
        map1[temp] = newNode 
        temp = temp.next 

    temp = head

    while temp is not None: 
        copiedNode = map1[temp] 
        randomNode = temp.random
        nextNode = temp.next if temp.next is not None else None
        copiedNode.random = map1[randomNode] if randomNode is not None else None
        copiedNode.next = map1[nextNode] if nextNode is not None else None 

        temp = temp.next 

    return map1[head]

def printClonedLinkedList(head):
    while head is not None:
        print(f"Data: {head.data}", end="")
        if head.random is not None:
            print(f", Random: {head.random.data}")
        else:
            print(", Random: nullptr")
        head = head.next


# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    clonedList = createCopy(head)

    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)