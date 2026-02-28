def recLongestCommonSubsequence(s1, s2, ind1, ind2): 
    if ind1 < 0 or ind2 < 0: 
        return 0 
    
    else: 
        if s1[ind1] == s2[ind2]: 
            return (1 + recLongestCommonSubsequence(s1, s2, ind1 - 1, ind2 - 1))
        else: 
            ind1move = 0 + recLongestCommonSubsequence(s1, s2, ind1 - 1, ind2) 
            ind2move = 0 + recLongestCommonSubsequence(s1, s2, ind1, ind2 - 1) 

            return max(ind1move, ind2move) 
         

def longestCommonSubsequenceTabulated(s1, s2): 
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)] 
    for i in range(len(s1) + 1): 
        dp[i][0] = 0 
    
    for k in range(len(s2) + 1): 
        dp[0][k] = 0

    for index1 in range(1, len(s1) + 1): 
        for index2 in range(1, len(s2) + 1): 
            if s1[index1 - 1] == s2[index2 - 1]: 
                dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1] 
            else: 
                ind1move = dp[index1 - 1][index2] 
                ind2move = dp[index1][index2 - 1] 

                dp[index1][index2] = max(ind1move, ind2move) 
    
    return dp[len(s1)][len(s2)]