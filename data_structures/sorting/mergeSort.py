def merge(list1, low, mid, high): 
    pass 


def mergeSort(list1, low, high): 
    if (low >= high):
        return 
    
    mid = low + high // 2
    mergeSort(list1, low, mid) 
    mergeSort(list1, mid+1, high) 
    merge(list1, low, mid, high) 



print(3//2); 
