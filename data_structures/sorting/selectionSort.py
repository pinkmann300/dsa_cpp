def selectionSort(list1):  
    for i in range(0, len(list1)): 
        miniIndex = i 
        for j in range(i + 1, len(list1)): 
            if (list1[j] < list1[miniIndex]): 
                miniIndex = j 
            
        temp = list1[i] 
        list1[i] = list1[miniIndex] 
        list1[miniIndex] = temp 
    
    return list1 

list1 = [2,3,4,5,62,11,2,12,]
list1 = selectionSort(list1) 
print(list1) 

