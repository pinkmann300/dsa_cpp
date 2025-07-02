class Stack:
    def __init__(self):
        self.size = 1000; 
        self.arr = [-1] * self.size
        self.top = -1
               
    def push(self, x):
        self.top += 1
        self.arr[self.top] = x 

    def getTop(self):
        return self.arr[self.top]
    
    def pop(self):
        k = self.arr[self.top]
        self.top -= 1
        return k
    
    def getSize(self):
        return self.top + 1
    

# Main program goes here 
    
if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.getTop())
    print("Size of stack before deleting any element", s.getSize())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.getSize())
    print("Top of stack after deleting an element", s.getTop())
