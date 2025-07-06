class Stack: 
    def __init__(self, size):
        self.size = size 
        self.arr = [None] * size 
        self.__top = -1 
        self.currentSize = 0 

    def isEmpty(self): 
        return (self.currentSize == 0)

    def push(self, x): 
        #Edge cases : 
        #If stack is full, print out saying stack is full 

        if (self.currentSize == self.size): 
            print("Stack is full. You cannot push more elements") 
            exit(1)

        self.__top += 1
        self.arr[self.__top] = x 
        self.currentSize += 1 
        return self 
    

    def top(self): 
        if (self.currentSize != 0):
            return self.arr[self.__top]
        else: 
            print("Stack is empty") 
        
    def pop(self): 
        if (self.isEmpty()): 
            print("Empty stack, no elements to pop") 
            exit(1)
        
        value = self.arr[self.__top]
        self.__top -= 1 
        self.currentSize -= 1 
        return value
    
    def length(self): 
        return self.currentSize 
    

if __name__ == "__main__":
    s = Stack(5)
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.top())
    print("Size of stack before deleting any element", s.length())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.length())
    print("Top of stack after deleting an element", s.top())
    

