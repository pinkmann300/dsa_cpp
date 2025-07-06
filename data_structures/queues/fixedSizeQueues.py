#The size of the queue is fixed. 

class Queue: 
    def __init__(self, size): 
        self.size = size
        self.queue = [] 
        self.__top = -1 
        self.__last = -1
        self.currentSize = 0

    def push(self, x): 
        #Queue full case: 
        if (self.currentSize == self.size): 
            print("Queue is full")
            exit(1) 

        #Queue empty case: 
            #Since it is a queue, we have to start pushing to the end of the list. 
            #Since it is a fixed size queue, we will have to start taking the modulo 
            #of the same 

        self.__last += 1 
        self.queue[self.__last % self.size] = x
        self.currentSize += 1
        return self  

    def pop(self): 
        pass 

    def top(self): 
        pass 

    def isEmpty(self): 
        return (self.currentSize == 0)

    def currentSize(self): 
        pass 
         
         
