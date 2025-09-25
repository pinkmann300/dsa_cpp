def distinctSubRec(ind1, ind2, s1, s2):
    if ind2 < 0: 
        return 1 
    if ind1 < 0: 
        return 0 
    
    if (s1[ind1] == s2[ind2]): 
        taken = distinctSubRec(ind1 - 1, ind2 - 1, s1, s2) 
        notTaken = distinctSubRec(ind1 - 1, ind2, s1, s2) 
        return taken + notTaken
    else: 
        return distinctSubRec(ind1 - 1, ind2, s1, s2) 
    

def distinctSubMemo(ind1, ind2, s1, s2, dp): 
    if ind2 < 0: 
        return 1 
    if ind1 < 0: 
        return 0 
    
    if dp[ind1][ind2] != -1: 
        return dp[ind1][ind2] 
    
    if (s1[ind1] == s2[ind2]): 
        taken = distinctSubMemo(ind1 - 1, ind2 - 1, s1, s2, dp)
        notTaken = distinctSubMemo(ind1 - 1, ind2, s1, s2, dp)  
        dp[ind1][ind2] = taken + notTaken 
        return dp[ind1][ind2]
    else: 
        dp[ind1][ind2] = distinctSubMemo(ind1 - 1, ind2, s1, s2, dp)    
        return dp[ind1][ind2] 
    


s1 = "babgbag"
s2 = "bag"

dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))] 
print(distinctSubMemo(len(s1) - 1, len(s2) - 1, s1, s2, dp))

# Calculate and print the count of distinct subsequences
print("The Count of Distinct Subsequences is", distinctSubRec(len(s1) - 1, len(s2) - 1,s1, s2))