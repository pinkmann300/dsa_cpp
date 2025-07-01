class Node: 
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

def printLL (head: Node):
    while (head != None):
        print(head.data, "->", end="")
        head = head.next 

def revLL(head, k):
    temp = head 
    count = 0
    while (temp != None or count == k):
        temp = temp.next 
        count += 1
        
        