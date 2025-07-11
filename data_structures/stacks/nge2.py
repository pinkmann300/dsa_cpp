# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array,
# which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.


def nextGreaterElement(nums1, nums2): 
    ngeStack = [] 
    ngeDict = {} 

    for i in range(2 * len(nums2) - 1, -1, -1): 
        
        while (ngeStack and ngeStack[len(ngeStack) - 1] <= nums2[i % len(nums2)]): 
            ngeStack.pop() 

        if (i < len(nums2)): 
            if (ngeStack): 
                ngeDict[nums2[i]] = ngeStack[len(ngeStack) - 1]
        
        ngeStack.append(nums2[i % len(nums2)]) 

    finalArr = [] 

    for k in nums1: 
        finalArr.append(ngeDict[k]) 

    return finalArr
        
