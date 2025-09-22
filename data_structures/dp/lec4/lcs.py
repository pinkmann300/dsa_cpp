def longestCommonSub(s1, s2, ind1, ind2): 
    if (ind1 < 0 or ind2 < 0): 
        return 0 
    if (s1[ind1] == s2[ind2]): 
        return 1 + longestCommonSub(s1,s2, ind1 - 1, ind2 - 1) 
    else: 
        s1Inclu = 0 + longestCommonSub(s1,s2, ind1 - 1, ind2) 
        s2Inclu = 0 + longestCommonSub(s1,s2, ind1, ind2 - 1) 
        return 0 + max(s1Inclu, s2Inclu)
    
def longestCommonSubMemo(s1, s2, ind1, ind2, dp): 
    if (ind1 < 0 or ind2 < 0): 
        return 0 
    if (s1[ind1] == s2[ind2]): 
        return 1 + longestCommonSubMemo(s1, s2, ind1 - 1, ind2 - 1, dp) 
    if (dp[ind1][ind2] != -1): 
        return dp[ind1][ind2] 
    else: 
        s1Included = 0 + longestCommonSubMemo(s1, s2, ind1 - 1, ind2, dp) 
        s2Included = 0 + longestCommonSubMemo(s1, s2, ind1, ind2 - 1, dp) 
        dp[ind1][ind2] = max(s1Included, s2Included) 
    return dp[ind1][ind2] 

def longestCommonSubTabulation(s1, s2):
    ind1 = len(s1) 
    ind2 = len(s2) 

    dp = [[0 for _ in range(ind2 + 1)] for _ in range(ind1 + 1)] 

    for index1 in range(1,ind1 + 1): 
        for index2 in range(1,ind2 + 1): 
            if (s1[index1 - 1] == s2[index2 - 1]): 
                dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1] 
            else: 
                indexMoves = max(dp[index1 - 1][index2], dp[index1][index2 - 1]) 
                dp[index1][index2] = indexMoves
    return dp[ind1][ind2]

def lcsMemoStart(s1, s2): 
    ind1 = len(s1) - 1 
    ind2 = len(s2) - 1 
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))] 
    return longestCommonSubMemo(s1, s2, ind1, ind2, dp) 

def printlongestCSubRec(s1, s2, ind1, ind2, cs): 
    if (ind1 < 0 or ind2 < 0): 
        return cs
    if (s1[ind1] == s2[ind2]): 
        return printlongestCSubRec(s1, s2, ind1 - 1, ind2 - 1, s1[ind1] + cs) 
    else: 
        s1Inclu = printlongestCSubRec(s1, s2, ind1 - 1, ind2, cs) 
        s2Inclu = printlongestCSubRec(s1, s2, ind1, ind2 - 1, cs) 
        maxVal = "" 
        if (len(s1Inclu) > len(s2Inclu)): 
            maxVal = s1Inclu 
        else: 
            maxVal = s2Inclu 

        return maxVal

def printlongestCommonSubTabulation(s1, s2):
    ind1 = len(s1) 
    ind2 = len(s2) 

    dp = [[0 for _ in range(ind2 + 1)] for _ in range(ind1 + 1)] 

    for index1 in range(1,ind1 + 1): 
        for index2 in range(1,ind2 + 1): 
            if (s1[index1 - 1] == s2[index2 - 1]): 
                dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1] 
            else: 
                indexMoves = max(dp[index1 - 1][index2], dp[index1][index2 - 1]) 
                dp[index1][index2] = indexMoves
    i = ind1 - 1
    j = ind2 - 1

    stringRet = "" 


    while (i >= 0 and j >= 0): 
        if (s1[i] == s2[j]): 
            stringRet = s1[i] + stringRet 
            i = i - 1 
            j = j - 1 
        else: 
            left = dp[i][j - 1]
            up = dp[i - 1][j] 
            if (left > up): 
                j = j - 1 
            else: 
                i = i - 1

    return stringRet

print(printlongestCommonSubTabulation("adebc", "dcadb")) 