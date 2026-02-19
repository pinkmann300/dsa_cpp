def nMeetings(start, end): 
    meetings = [(end[i], start[i], i + 1) for i in range(len(start))] 
    meetings.sort() 
    #Time complexity O(n log n) 

    count = 0
    results = [] 
    endTime = -1   

    for endt, startt, idx in meetings: 
        if startt >= endTime: 
            endTime = endt 
            count += 1 
            results.append(idx) 

    return count 

#Language based learning is that if I have a list of tuples and I try to sort it, 
#it sorts based on the first element in the tuple. 


"""
Example 1:
Input:nums = [2, 3, 1, 0, 4]
Output: True           
Explanation: 
We start at index 0, with value 2 this means we can jump to index 1 or 2.
From index 1, with value 3, we can jump to index 2, 3, or 4. However, if we jump to index 2 with value 1, we can only jump to index 3.
So we jump to index 1 then index 4 reaching the end of the array.
Hence, we return true.

"""
def jumpGame(arr): 
    maximumIndexReached = 0 
    currentIndex = 0 

    while currentIndex <= maximumIndexReached: 
        maximumIndexReached += arr[currentIndex]
        if maximumIndexReached >= len(arr) - 1: 
            return True 

    return False 
 

nums = [3,2,1,0,4] 
print(jumpGame(nums))


