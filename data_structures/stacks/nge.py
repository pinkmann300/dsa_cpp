def nextGreaterElement(list1): 
    ngeList = [-1] * len(list1)
    ngeStack = [] 

    for i in range(len(list1) - 1, -1, -1):
        while (ngeStack and ngeStack[-1] <= list1[i]): 
            ngeStack.pop()


        ngeElement = -1 if not ngeStack else ngeStack[-1] 
        ngeStack.append(list1[i]) 
        ngeList[i] = ngeElement

    return ngeList 


nums2 = [1,2,3,0,9]
print(nextGreaterElement(nums2))