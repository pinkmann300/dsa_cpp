#The size of the queue is fixed. 

class Queue: 
    def __init__(self, size): 
        self.size = size
        self.queue = [None] * size
        self.__top = -1 
        self.__last = -1
        self.currentSize = 0
 
    def push(self, x): 
        #Queue full case: 
        if (self.currentSize == self.size): 
            print("Queue is full, cannot push more elements")
            exit(1) 

        #Queue empty case: 
            #Since it is a queue, we have to start pushing to the end of the list. 
            #Since it is a fixed size queue, we will have to start taking the modulo 
            #of the same
        if (self.__last == -1): 
            self.__top = 0 
            self.__last = 0
        else: 
            self.__last = (self.__last + 1) % self.size
            
        self.queue[self.__last] = x 
        self.currentSize += 1 

        return self 


       

    def pop(self): 
        if (self.currentSize == 0): 
            print("Queue is empty, no elements to pop")
            exit(1)

        if (self.currentSize == 1): 
            topIndex = (self.__top) % self.size 
            value = self.queue[topIndex] 
            self.__top = -1
            self.__last = -1 
            self.currentSize = 0
            return value 
        
        else: 
            self.__top = (self.__top + 1) % self.size 
            self.currentSize += 1 

        return self 
    
    def top(self): 
        if (self.isEmpty()): 
            print("Queue is empty") 
            exit(1) 
        return (self.queue[self.__top])
    
    def isEmpty(self): 
        return (self.currentSize == 0)

    def length(self): 
        return (self.currentSize) 
         
         
if __name__ == "__main__":
    q = Queue(10)
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.length())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.length())