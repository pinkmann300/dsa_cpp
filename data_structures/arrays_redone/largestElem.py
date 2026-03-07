def largestElement(arr): 
    maxVal = float('-inf') 
    for i in arr: 
        maxVal = max(maxVal, i) 
    
    return maxVal

def secondLargestElement(arr): 
    largestElem = arr[0] 
    secondLargestElem = float('-inf') 

    for i in range(1, len(arr)): 
        if arr[i] > largestElem: 
            secondLargestElem = largestElem 
            largestElem = arr[i] 
        
        elif (arr[i] > secondLargestElem) and (arr[i] != largestElem) and (arr[i] < largestElem): 
            secondLargestElem = arr[i] 

    return secondLargestElem 

def linearSearch(k, nums): 
    for i in range(len(nums)):  
        if nums[i] == k:
            return i 
        
    return -1  