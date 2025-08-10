def merge(list1, low, mid, high): 
    temp = [] 
    left = low 
    right = mid + 1 

    while (left <= mid and right <= high): 
        if (list1[left] <= list1[right]): 
            temp.append(list1[left]) 
            left += 1 
        else: 
            temp.append(list1[right])
            right += 1

    while (left <= mid): 
        temp.append(list1[left]) 
        left += 1 
    
    while (right <= high): 
        temp.append(list1[right])
        right += 1

    for i in range(low, high + 1): 
        list1[i] = temp[i - low]
    

def mergeSort(list1, low, high): 
    if (low >= high):
        return 
    
    mid = (low + high) // 2
    mergeSort(list1, low, mid) 
    mergeSort(list1, mid+1, high) 
    merge(list1, low, mid, high)

list1= [239,2923,102101,9201,292033,391] 
mergeSort(list1, 0, len(list1) - 1) 
print(list1)