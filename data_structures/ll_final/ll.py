# The final version of linked list work.

class Node: 
    def __init__(self, data, next = None): 
        self.data = data 
        self.next = next 

def pushElement(head, val): 
    newHead = Node(val,head) 
    return newHead

def insertAtEnd(head, val): 
    temp = head

    if temp is None: 
        head = Node(val, head)
        return head 
    
    while (temp.next is not None): 
        temp = temp.next 
    temp.next = Node(val, None) 
    return head 


#Time complexity: O(n)
#Space complexity: O(1) 
def deleteTail(head): 
    if (head is None or head.next is None): 
        return None 
    temp = head 
    while (temp.next.next is not None): 
        temp = temp.next 
    temp.next = None 
    return head 

#Space complexity: O(1) 
#Time complexity: O(n)
def lengthOfList(head): 
    count = 0 
    temp = head
    while (temp is not None): 
        count += 1 
        temp = temp.next 
    return count   

def searchElement(head, target): 
    temp = head 
    while (temp is not None): 
        if (temp.val == target): 
            return True 
        temp = temp.next  
    return False     

def printLL(head):
    while head is not None: 
        print(head.data, "->", end="")
        head = head.next 

if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 100

    # Creating a linked list with initial elements from the array
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Inserting a new node at the head of the linked list
    head = pushElement(head, val)
    # Printing the linked list
    printLL(head)







