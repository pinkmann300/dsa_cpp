class Node:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = None 

def reverseLL(head: Node):
    current = head 
    prev = None 
    while (current != None):
        temp = current.next 
        current.next = prev
        prev = current 
        current = temp 

    return prev 

def palindromeCheck(head):
    fast = head 
    slow = head 

    while (fast.next != None and fast.next.next != None):
        slow = slow.next 
        fast = fast.next.next 

    latterNode = reverseLL(slow.next)
    
    p1 = head 
    p2 = latterNode

    while (p2 != None):
        if (p1.data != p2.data):
            return False
        p1 = p1.next
        p2 = p2.next 

    return True


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def main():
    # Create a linked list with
    # values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if palindromeCheck(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

if __name__ == "__main__":
    main()