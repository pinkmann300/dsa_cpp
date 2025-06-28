class Node: 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def detectLoop(head : Node):
    slow = head 
    fast = head 
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next 

        if (fast == slow):
            return True
    
    return False


if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if detectLoop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")
