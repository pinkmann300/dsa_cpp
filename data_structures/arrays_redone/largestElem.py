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

def unionOfTwoSortedArrays(nums1, nums2): 
    len1 = len(nums1) 
    len2 = len(nums2) 

    num1Index, num2Index = 0, 0 
    unionArray = [] 

    while num1Index < len1 and num2Index < len2: 
        if nums1[num1Index] > num2Index[num2Index] and unionArray and unionArray[-1] != nums2[num2Index]: 
            unionArray.append(nums2[num2Index]) 
            num2Index += 1 
        
        elif nums1[num1Index] < num2Index[num2Index] and unionArray and unionArray[-1] != nums1[num1Index]:
            unionArray.append(nums1[num1Index]) 
            num1Index += 1

    return unionArray

def missingNumber(nums1): 
    n1 = len(nums1) + 1
    totalSum = sum(nums1) 
    expectedSum = (n1 * (n1 + 1)) // 2 
    return expectedSum - totalSum 



arr1 = [1,2,3,4,5,7]  
print(missingNumber(arr1)); 