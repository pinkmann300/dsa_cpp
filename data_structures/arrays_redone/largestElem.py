def largestElement(arr): 
    maxVal = float('-inf') 
    for i in arr: 
        maxVal = max(maxVal, i) 
    
    return maxVal