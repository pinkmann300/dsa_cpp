
#The below solution is a brute force solution. 
def countInversions(nums): 
    count = 0 
    for i in range(len(nums)): 
        for j in range(i + 1, len(nums)): 
            if nums[i] > nums[j]:
                count += 1
    return count 

def mergeSort(nums, low, high): 
    cnt = 0 

    if low >= high: 
        return cnt 
    
    mid = (low + high) // 2 

    cnt += mergeSort(nums, low, mid) 
    cnt += mergeSort(nums, mid + 1, high) 
    cnt += merge(nums, low, mid, high)
    return cnt 

def merge(nums, l, m, h): 
    pass 
