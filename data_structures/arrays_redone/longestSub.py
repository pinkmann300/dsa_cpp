def countSubarrays(nums, k): 
    prefixMap = {0 : 1} 
    prefix = 0 
    count = 0 

    for num in nums: 
        prefix ^= num 

        target = prefix ^ k 
        if target in prefixMap: 
            count += prefixMap[target] 

        prefixMap[prefix] = prefixMap.get(prefix, 0) + 1

    return count 