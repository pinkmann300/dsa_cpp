#The below program computes the number of elements which are greater than 
#a given element in an array.


def numberOfNGEs(nums1, nums2): 
    
    ngeDict = {} 
    ngeStack = [] 
    for i in range(len(nums2) - 1, -1, -1): 
        while (ngeStack and ngeStack[len(ngeStack) - 1] <= nums2[i]): 
            ngeStack.pop() 

        ngeDict[nums2[i]] = len(ngeStack) 
        ngeStack.append(nums2[i]) 

    finalArr = [] 

    for ko in nums1: 
        finalArr.append(ngeDict[ko])

    return finalArr


if __name__ == "__main__": 
    nums2 = [1,2,3,4,5,6,7,8] 
    nums1 = [3,5]

    print(numberOfNGEs(nums1, nums2))
