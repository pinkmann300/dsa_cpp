class Car: 
    def __init__(self, carName, carId): 
        self.__carName = carName  
        self.__carId = carId


object1 = Car("Sandeep", "1") 
print(type(object1)) 

print(type(20))

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

def maximumConsecutiveOnes(nums1): 
    conOnes = 0 
    maxOnes = 0 
    for i in nums1: 
        if i == 1: 
            conOnes += 1 
            maxOnes = max(maxOnes, conOnes) 
        else: 
            conOnes = 0 
    return maxOnes

def majorityElement(nums1): 
    count = 0 
    elem = 0 

    for k in nums1: 
        if count == 0: 
            count += 1 
            elem = k 

        elif k != elem: 
            count -= 1 

    return elem

def rotateBy90(matrix): 
    newMatrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))] 
    for row in range(len(matrix)): 
        for col in range(len(matrix)): 
            newMatrix[col][len(matrix) - row - 1] = matrix[row][col] 

    return newMatrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotateBy90(matrix))
