class Node: 
    def __init__(self, val, next=None): 
        self.val = val 
        self.next = next

def reverseLinkedList(head): 
    if head is None or head.next is None: 
        return head 
    current = head 
    prev = None
    while current is not None: 
        temp = current.next 
        current.next = prev 
        prev = current
        current = temp 

    return prev 

def printLL(head): 
    while head is not None: 
        print(head.val, "->", end=" ") 
        head = head.next 

def findMiddle(head): 
    fast = head 
    slow = head 
    while (fast.next is not None or fast is not None): 
        fast = fast.next.next 
        slow = slow.next 
    return slow 

def detectLoop(head): 
    slow = head 
    fast = head 

    while (fast is not None or fast.next is not None): 
        fast = fast.next.next 
        slow = slow.next 

        if (fast == slow): 
            return True 
        
    return False 

def startingPointOfLoop(head): 
    fast = head 
    slow = head 
    while (fast.next is not None or fast is not None): 
        fast = fast.next.next 
        slow = slow.next 

        if (fast == slow): 
            slow = head 
            while (slow != fast): 
                slow = slow.next 
                fast = fast.next 
            return fast 
    return -1 

def lengthOfLoop(head): 
    fast = head 
    slow = head 
    while (fast.next is not None and fast is not None): 
        fast = fast.next.next
        slow = slow.next 

        if (fast == slow): 
            slow = slow.next
            count = 1
            while (slow != fast): 
                slow = slow.next 
                count = count + 1 
            return count 
    return 0 

def segregateOddEven(head): 
    evenHead = Node(-1)
    oddHead = Node(-1) 

    current = head
    oddTail = oddHead
    evenTail = evenHead

    while current is not None: 
        temp = current 
        current = current.next 
        temp.next = None 
        if (temp.val % 2 == 1): 
            oddTail.next = temp
            oddTail = oddTail.next 
        else: 
            evenTail.next = temp 
            evenTail = evenTail.next 

    evenTail.next = oddHead.next 
    return evenHead.next 

def deleteMiddle(head): 
    if head is None or head.next is None: 
        return None 

    fast = head.next.next 
    slow = head 

    while (fast is not None or fast.next is not None): 
        fast = fast.next.next 
        slow = slow.next 

    slow.next = slow.next.next 
    return head 

def sort012(head): 
    zeroList = Node(-1) 
    oneList = Node(-1) 
    twoList = Node(-1) 

    zeroTemp = zeroList 
    oneTemp = oneList 
    twoTemp = twoList 
    current = head 


    while current is not None: 
        temp = current.next
        current.next = None
        
        if (current.val == 0): 
            zeroTemp.next = current
            zeroTemp = zeroTemp.next 
        
        elif (current.val == 1): 
            oneTemp.next = current 
            oneTemp = oneTemp.next 

        elif (current.val == 2):
          
            twoTemp.next = current 
            twoTemp = twoTemp.next

        current = temp

    totalNode = Node(-1) 
    
    if (zeroList.next is not None):
        totalNode.next = zeroList.next

    if (oneList.next is not None): 
        zeroTemp.next = oneList.next 

    if (twoList.next is not None): 
        oneTemp.next = twoList.next 

    return totalNode.next 

def add1(head): 
    newHead = reverseLinkedList(head) 
    temp = newHead 
    sum = (temp.val + 1) % 10 
    carry = 1

    while (temp.next is not None): 
        sum = (temp.val + carry)
        carry = sum // 10 
        temp.val = sum % 10 
        temp = temp.next 
        if (carry == 0): 
            break

    if (carry == 0):
        return reverseLinkedList(newHead)
    else: 
        sum = (temp.val + carry) 
        carry = sum // 10 
        temp.val = sum % 10 
        temp.next = Node(carry) 
        return reverseLinkedList(newHead)
    
def add12(head): 
    newHead = reverseLinkedList(head) 
    temp = newHead 
    carry = 1 

    while carry is not None: 
        sum = (temp.val + carry) 
        temp.val = sum % 10 
        carry = sum // 10 

        if carry == 0: 
            return reverseLinkedList

        if (temp.next is None and carry != 0): 
            temp.next = Node(carry) 
            return reverseLinkedList(newHead) 
        
        temp = temp.next 
    
    return reverseLinkedList(newHead) 

def add2Num(head1, head2):
    l1 = head1 
    l2 = head2 
    carry = 0 

    ansHead = Node(-1) 
    ansTail = ansHead 

    while (l1 or l2 or carry): 
        sum = 0
        if (l1): 
            sum += l1.val
            l1 = l1.next 

        if (l2): 
            sum += l2.val 
            l2 = l2.next 

        sum += carry 

        ansTail.next = Node(sum % 10) 
        ansTail = ansTail.next 
        carry = sum // 10 

    return ansHead.next 

def intersectionPoint(head1, head2): 
    dummy1 = head1 
    dummy2 = head2 

    while (dummy1 != dummy2): 
        dummy1 = head2 if dummy1 is None else dummy1.next 
        dummy2 = head1 if dummy2 is None else dummy2.next 
    
    return dummy1 

def deleteDuplicates(head): 
    temp = head 
    while (temp is not None): 
        data = temp.val
        while (temp.next and temp.next.val == data): 
            temp.next = temp.next.next 
        temp = temp.next 
        
    return head 


head = Node(1, Node(1, Node(2, Node(2, Node(2, None)))))

# Check if there is a loop in the linked list
newHead = deleteDuplicates(head)
printLL(newHead)


