class Node :
    def __init__(self, data, next= None):
        self.data = data
        self.next = next 

def startingLoop(head : Node):
    slow = head 
    fast = head 

    while (fast != None and fast.next != None):
        fast = fast.next.next 
        slow = slow.next

        if (slow == fast):
            slow = head; 
            
            while (slow != fast):
                slow = slow.next
                fast = fast.next 

            return slow; 

    return None

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

# Detect the loop in the linked list
loop_start_node = startingLoop(head)

if loop_start_node:
    print("Loop detected. Starting node of the loop is:", loop_start_node.data)
else:
    print("No loop detected in the linked list.")
        
