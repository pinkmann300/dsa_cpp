# Implement Min Stack | O(2N) and O(N) Space Complexity. Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.


class MinStack: 
    def __init__(self):
        self.arr = []
        self.top = -1 

    def topEl(self): 
        valueObj = self.arr[self.top] 
        return valueObj 


    def push(self, x): 
        if (self.top == -1): 
            minElement = x 
            self.arr.append([x,minElement])
        else: 
            valueObj = self.topEl()
            if (valueObj[1] > x): 
                self.arr.append([x, x])
            else: 
                self.arr.append([x, valueObj[1]]) 

        self.top += 1
        return self 
    
    def pop(self): 
        self.arr.pop(self.top)
        self.top -= 1 
        return self 
    
    def isEmpty(self): 
        return (len(self.arr) == 0) 
    
    def getMin(self): 
        return (self.arr[self.top][1])
    


if __name__ == "__main__":
    newMin = MinStack()
    newMin.push(45)
    newMin.push(23)
    newMin.push(21)
    newMin.push(20)
    
    newMin.pop()
    newMin.pop()

    print(newMin.getMin())