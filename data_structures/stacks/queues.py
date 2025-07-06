#Simplest way to implemennt a queue using a list1. 

class Queue: 
    def __init__(self): 
        self.list1 = []
    
    def pushQueue(self, x): 
        self.list1.append(x)

    def popQueue(self, x): 
        self.list1.pop(0) 

    def length(self):
        return len(self.list1)
    
