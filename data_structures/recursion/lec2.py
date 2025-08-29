def recursiveSorted(arr): 
    if (len(arr) <= 1): 
        return True 
    else:
        if (arr[0] <= arr[1]): 
            return recursiveSorted(arr[1:]) 
        else: 
            return False 
        
def linearSearch(arr, index, target, results): 
    if (index == len(arr)): 
        return results
    else: 
        if arr[index] == target:
            return linearSearch(arr, index + 1, target, results + [index])  
        else: 
            return linearSearch(arr, index + 1, target, results)       

arr = [1,2,3,4,5,4]
print(linearSearch(arr, 0, 4, []))