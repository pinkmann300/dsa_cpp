def bubbleSort(list1): 
    for i in range(0, len(list1)): 
        for j in range(0, len(list1) - 1): 
            if (list1[j] > list1[j + 1]):
                temp = list1[j] 
                list1[j] = list1[j + 1] 
                list1[j + 1] = temp 
                
    return list1 

list1 = [2,3,4,5,62,11,2,12,]
list1 = bubbleSort(list1) 
print(list1) 
