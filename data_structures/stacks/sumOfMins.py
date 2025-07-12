#The problem will take care of the sum of minimums in a subarray 

def sumMinSubarray (nums1): 
    totalSum = 0 
    for i in range(0, len(nums1)): 
       minim = nums1[i]
       totalSum += nums1[i]  
       for j in range(i + 1, len(nums1)): 
           minim = min(minim, nums1[j]) 
           totalSum += minim 

    return totalSum  


if __name__=="__main__": 
    nums1 = [11,81,94,43,3]
    print(sumMinSubarray(nums1))



