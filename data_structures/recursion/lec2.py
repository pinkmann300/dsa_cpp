def recursiveSorted(arr): 
    if (len(arr) <= 1): 
        return True 
    else:
        if (arr[0] <= arr[1]): 
            return recursiveSorted(arr[1:]) 
        else: 
            return False 
        

arr = [1,2,3,4,5,4]
print(recursiveSorted(arr))