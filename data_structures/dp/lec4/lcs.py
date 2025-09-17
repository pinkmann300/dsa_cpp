def longestCommonSub(s1, s2, ind1, ind2): 
    if (ind1 < 0 or ind2 < 0): 
        return 0 
    
    if (s1[ind1] == s2[ind2]): 
        return 1 + longestCommonSub(s1,s2, ind1 - 1, ind2 - 1) 
    
    else: 
        s1Inclu = 0 + longestCommonSub(s1,s2, ind1 - 1, ind2) 
        s2Inclu = 0 + longestCommonSub(s1,s2, ind1, ind2 - 1) 
        return 0 + max(s1Inclu, s2Inclu)
    

def longestCSubRec(s1, s2, ind1, ind2, cs): 
    if (ind1 < 0 or ind2 < 0): 
        return cs
    if (s1[ind1] == s2[ind2]): 
        return longestCSubRec(s1, s2, ind1 - 1, ind2 - 1, s1[ind1] + cs) 
    else: 
        s1Inclu = longestCSubRec(s1, s2, ind1 - 1, ind2, cs) 
        s2Inclu = longestCSubRec(s1, s2, ind1, ind2 - 1, cs) 
        maxVal = "" 
        if (len(s1Inclu) > len(s2Inclu)): 
            maxVal = s1Inclu 
        else: 
            maxVal = s2Inclu 

        return maxVal     

print(longestCSubRec("adebc", "dcadb", 4, 4, ""))