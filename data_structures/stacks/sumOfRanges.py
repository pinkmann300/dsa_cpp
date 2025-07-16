#The problem will take care of the sum of minimums in a subarray 
#The below is the brute force approach for 
def sumMinSubarray (nums1): 
    totalSum = 0 
    for i in range(0, len(nums1)): 
       minim = nums1[i]
       totalSum += nums1[i]  
       for j in range(i + 1, len(nums1)): 
           minim = min(minim, nums1[j]) 
           totalSum += minim 

    return totalSum  

def nextSmallerIndex(nums1): 
    nseStack = []
    nseIndexArr = [-1] * len(nums1) 
    for i in range(len(nums1) - 1, -1, -1): 
        while (nseStack and nums1[nseStack[-1]] >= nums1[i]): 
            nseStack.pop() 

        nseIndex = len(nums1) if not nseStack else nseStack[-1] 
        nseStack.append(i)
        nseIndexArr[i] = nseIndex
    return nseIndexArr   


def previousSmallerIndex(nums1): 
    pseStack = [] 
    pseIndexArr = [None] * len(nums1) 
    for i in range(0, len(nums1)): 
        while (pseStack and nums1[pseStack[-1]] > nums1[i]): 
            pseStack.pop() 
        pseIndex = -1 if not pseStack else pseStack[-1] 
        pseStack.append(i) 
        pseIndexArr[i] = pseIndex
    return pseIndexArr    


def sumOfMins(nums1): 
    pseArr = previousSmallerIndex(nums1) 
    nseArr = nextSmallerIndex(nums1) 
    totalSum = 0  
    for i in range(len(nums1)): 
       left = i - pseArr[i] 
       right = nseArr[i] - i 
       contribution = left * right * nums1[i] 
       totalSum += contribution  
    return totalSum

def previousGreaterIndex(nums1):
    pseStack = [] 
    pseIndexArr = [None] * len(nums1) 
    for i in range(0, len(nums1)): 
        while (pseStack and nums1[pseStack[-1]] < nums1[i]): 
            pseStack.pop() 
        pseIndex = -1 if not pseStack else pseStack[-1] 
        pseStack.append(i) 
        pseIndexArr[i] = pseIndex
    return pseIndexArr

def nextGreaterIndex(nums1): 
    nseStack = []
    nseIndexArr = [-1] * len(nums1) 
    for i in range(len(nums1) - 1, -1, -1): 
        while (nseStack and nums1[nseStack[-1]] <= nums1[i]): 
            nseStack.pop() 

        nseIndex = len(nums1) if not nseStack else nseStack[-1] 
        nseStack.append(i)
        nseIndexArr[i] = nseIndex
    return nseIndexArr  



def sumOfMaxes(nums1): 
    pgeArr = previousGreaterIndex(nums1) 
    ngeArr = nextGreaterIndex(nums1) 
    totalSum = 0  
    for i in range(len(nums1)): 
       left = i - pgeArr[i] 
       right = ngeArr[i] - i 
       contribution = left * right * nums1[i] 
       totalSum += contribution  
    return totalSum


def sumOfRanges(nums1): 
    minSum = sumOfMins(nums1)
    maxSum = sumOfMaxes(nums1) 

    return maxSum - minSum

if __name__=="__main__": 
    nums1 = [4,-2,-3,4,1]
    newSum = sumOfRanges(nums1) 
    print(newSum)
    



