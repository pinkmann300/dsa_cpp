class Queue: 
    def __init__(self): 
        self.front = 0
        self.rear = 0
        self.size = 5
        self.arr = [-1] * self.size 
        self.count = 0; 
    

    def push(self, x):
        if (self.count == self.size):
            print("Queue is full")
            exit(1)
       
        if (self.end == -1):
            self.rear = 0
            self.front = 0
        else:
            self.end = (self.end + 1) % self.size
            
        self.arr[self.end] = x 
        print("Element has been pushed")
        self.count += 1

    def pop(self, x):
        if (self.front == -1):
            print("Queue is empty")
            exit(1)

        value = self.arr[self.front]
        if (self.count == 1):
            self.start = -1 
            self.end  = -1 

        else :
            self.start = (self.start + 1) % self.size

        self.count -= 1



    def pop(self,x):
        value = self.arr[self.top]
        self.top =  self.top + 1
        self.count = self.count - 1
        return value 
    
    def top(self):
        if (self.front == -1):
            print("Queue is empty")
            exit(1)

        return self.arr[self.front]
    
    def sizeOfq(self):
        return self.count
    

if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())
    

        

    

    