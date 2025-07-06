#Implement unlimited size queues. 

class Queue: 
    def __init__(self): 
        self.queue = [] 

    def isEmpty(self): 
        return (len(self.queue) == 0)
    
    def push(self, x): 
        self.queue.append(x) 
        return self
    
    def top(self): 
        return self.queue[0]

    def pop(self): 
        value = self.queue.pop(0) 
        return value
    
    def length(self): 
        return (len(self.queue)) 


if __name__ == "__main__":  
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.length())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.length())