
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLL(l1): 
        current = l1 
        prev = None 

        while current: 
            temp = current.next 
            current.next = prev 
            prev = current 
            current = temp 

        return prev 

def addTwoNumbers(l1, l2):
        
        val1 = reverseLL(l1)
        val2 = reverseLL(l2) 
        carry = 0

        val3 = ListNode(-1)
        head = val3

        while (val1 and val2): 
            totalSum = val1.val + val2.val + carry 
            nodeSum = totalSum % 10 
            carry = totalSum // 10 
            head.next = ListNode(nodeSum)
            head = head.next
            val1 = val1.next 
            val2 = val2.next 

        while (val1): 
            totalSum = val1.val + carry 
            nodeSum = totalSum % 10 
            carry = nodeSum // 10 
            head.next = ListNode(nodeSum)
            head = head.next 
            val1 = val1.next 
            
        while (val2): 
            totalSum = val2.val + carry 
            nodeSum = totalSum % 10 
            carry = nodeSum // 10
            head.next = ListNode(nodeSum)
            head = head.next
            val2 = val2.next 

        while (carry != 0): 
            nodeSum = carry % 10 
            carry = carry // 10
            head.next = ListNode(nodeSum) 
            head = head.next
            
        return reverseLL(val3.next)


def printLL(val1): 
    while (val1): 
        print(val1.val , " -> ")
        val1 = val1.next 


if __name__ == "__main__":
    l1 = ListNode(5) 
    l2 = ListNode(5) 
    l3 = addTwoNumbers(l1, l2) 
    printLL(l3)