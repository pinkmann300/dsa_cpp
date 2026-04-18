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


#Longest repeating character replacement 

def lrcr(stringVal, k): 
    longestSubStringLength = 0 
    for i in range(len(stringVal)): 
        hashArray = [0 for _ in range(26)] 
        maxFrequency = 0

        for j in range(i, len(stringVal)): 
            hashArray[ord(stringVal[j]) - ord('A')] += 1 
            maxFrequency = max(maxFrequency, hashArray[stringVal[j] - 'A'])
            changes = (j - i + 1) - maxFrequency 
            if changes <= k: 
                longestSubStringLength = max(longestSubStringLength, j - i + 1) 
            else: 
                break 

#Complexity analysis : O(n^2) 

def lrcrOptimized(stringVal, k): 
    l = 0 
    r = 0
    maxFrequency = 0 
    maxLength = 0 
    hashMap = {} 

    stringLength = len(stringVal) 

    while r < stringLength: 
        if stringVal[r] not in hashMap: 
            hashMap[stringVal[r]] = 1 
        else: 
            hashMap[stringVal[r]] += 1 
            

        
        maxFrequency = max(maxFrequency, hashMap[stringVal[r]]) 

        currentLength = r - l + 1 
        conversionsRequired = currentLength - maxFrequency 

        if conversionsRequired <= k: 
            maxLength = max(maxLength, currentLength) 

        else: 
            lVal = stringVal[l] 
            hashMap[lVal] -= 1 
            l += 1 

        r += 1 

    return maxLength

