#Implement Min Stack | O(1) Time complexity and O(N) Space Complexity. Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack: 
    def __init__(self): 
        self.arr = [] 
        self.top = -1 
        self.minElement = -1 


    def isEmpty(self): 
        return (len(self.arr) == 0) 
    

    def push(self, x): 
        if (self.top == -1): 
            print("Stack is empty") 
            self.minElement = x
            self.arr.append(x) 
        else:
            if (x >= self.minElement): 
                self.arr.append(x) 
            else: 
                modElement = (2 * x) - self.minElement
                self.arr.append(modElement) 
                self.minElement = x 
        self.top += 1 


    def getTop(self): 
        if (self.arr[self.top] < self.minElement): 
            return self.minElement 
        else:
            return self.arr[self.top] 
        

    def pop(self) : 
        if (self.isEmpty()): 
            print("Stack is empty")
            exit(1) 
     
        if (self.getTop() < self.minElement): 
            newMin = (2 * self.minElement) - (self.getTop()) 
            self.minElement = newMin 
            self.arr.pop() 
            self.top -= 1 

        return self 

if __name__ == "__main__": 
    ms = MinStack()
    ms.push(10) 

    print(ms.top)

    ms.push(20)
    print(ms.arr)
    ms.push(2) 
    print(ms.top)
    ms.push(1)
    
        