def nge(arr): 
    ngeStack = [] 
    ngeList = [-1] * len(arr) 
    for i in range(len(arr) - 1, -1, -1): 
        while ngeStack and ngeStack[-1] <= arr[i]: 
            ngeStack.pop() 

        ngeElem = -1 if not ngeStack else ngeStack[-1] 
        ngeStack.append(arr[i]) 
        ngeList[i] = ngeElem 

    return ngeList

arr = [1,3,4,2]
print(nge(arr)) 

