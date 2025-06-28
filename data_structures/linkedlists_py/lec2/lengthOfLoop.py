class Node:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

def lengthOfLoop(head: Node):
    slow = head 
    fast = head 
    while (fast is not None and fast.next is not None):
        fast = fast.next.next 
        slow = slow.next 

        if (slow == fast):
            fast = fast.next 
            length = 1
            while (slow != fast):
                fast = fast.next
                length += 1

            return length 
        
    return 0

def find_loop_length(head):
    slow = head
    fast = head

    # Step 1: Traverse the list to detect a loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next     
        # Move fast two steps
        fast = fast.next.next  

        # Step 2: If the slow and fast
        # pointers meet, there is a loop
        if slow == fast:
            # Initialize the loop length
            length = 1  
             # Move fast one step
            fast = fast.next 

            # Step 4: Initialize a counter
            # and traverse using the fast pointer
            while slow != fast:
                # Move fast one step
                fast = fast.next  
                # Increment the counter
                length += 1  

            # Step 6: Return the 
            # length of the loop
            return length

    # Step 3: If the fast pointer
    # reaches the end, there is no loop
    return 0

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  
length = find_loop_length(head)
print(f"The length of the loop is: {length}")