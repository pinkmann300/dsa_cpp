#Similar to next greater element and this problem handles the smaller version of it. 


def nextSmallerElement(nums1, nums2): 
    nseDict = {} 
    nseStack = [] 

    for i in range(len(nums2) - 1, -1, -1): 
        elem = nums2[i] 
        while (nseStack and nseStack[len(nseStack) - 1] >= elem): 
            nseStack.pop()

        nseDict[elem] = nseStack[len(nseStack) - 1] if nseStack else -1 
        nseStack.append(elem)

    finalArr = []
    for k in nums1: 
        finalArr.append(nseDict[k]) 

    return finalArr


if __name__ == "__main__": 
    nums1 = [1,2,3] 
    nums2 = [3,2,1,-2,-3]

    print(nextSmallerElement(nums1, nums2)) 
    

        

