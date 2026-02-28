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
         

