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

