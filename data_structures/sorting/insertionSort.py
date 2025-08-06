def insertionSort(list1): 
    for i in range(0, len(list1)): 
        j = i 
        while (j > 0 and list1[j-1] > list1[j]): 
            temp = list1[j - 1] 
            list1[j - 1] = list1[j] 
            list1[j] = temp
            j = j - 1

    return list1 


list1 = [2,3,4,5,62,11,2,12,]
list1 = insertionSort(list1) 
print(list1) 