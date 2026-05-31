class BinaryHeap: 

    #Min heap implementation
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.arr = [0 for _ in range(capacity)] 


    def findParent(self, ind): 
        return (ind - 1) // 2 
    
    def leftChild(self, ind): 
        return ((2 * ind) + 1) 
    
    def rightChild(self, ind): 
        return ((2 * ind) + 2) 

 
    def insertIntoMinHeap(self, val): 
        #Check if there is space in the array. 
        if self.size == self.capacity: 
            exit("Binary Heap Overflow") 
            return 
        
        self.arr[self.size] = val 
        insertionIndex = self.size 
        parentIndex = self.findParent(self, insertionIndex) 
        
        while insertionIndex >= 0 and parentIndex >= -1 and self.arr[parentIndex] > self.arr[insertionIndex]: 
            self.arr[insertionIndex] , self.arr[parentIndex] = self.arr[parentIndex], self.arr[insertionIndex] 
            insertionIndex = parentIndex
            parentIndex = self.findParent(insertionIndex)

        self.size += 1 

    def getMinimum(self):
        return self.arr[0] 
    
    def heapify(self, ind): 
        smallest = ind 
        left_index = self.leftChild(ind) 
        right_index = self.rightChild(ind)

        if left_index < self.size and self.arr[left_index] < self.arr[smallest]: 
            smallest = left_index   

        if right_index < self.size and self.arr[right_index] < self.arr[smallest]: 
            smallest = right_index  

        if smallest != ind: 
            self.arr[smallest] , self.arr[ind] = self.arr[ind], self.arr[smallest] 
            self.heapify(smallest)

        #Perfect understanding thank you baby love you 
            

def checkMinHeap(heap): 
    #Min heap - property states that value of the children must be lesser than the ancestors 
    heapSize = heap.size 

    for i in range(0, (heapSize // 2)): 
        leftChild = (2 * i) + 1 
        rightChild = (2 * i) + 2 

        if leftChild < heapSize and heap.arr[leftChild] < heap.arr[i]: 
            return False 

        if rightChild < heapSize and heap.arr[rightChild] < heap.arr[i]: 
            return False 
        
    return True  
