def largestOddElem(s): 
    wordLen = len(s) 
    latestIndex = -1 

    for i in range(wordLen - 1, -1, -1): 
        if s[i] % 2 == 1: 
            latestIndex = i 
            break 

    word = str(int(s[0: latestIndex + 1])) 
    return word