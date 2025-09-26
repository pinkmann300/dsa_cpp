def editDistance(ind1, ind2, s1, s2): 
    if (ind1 < 0): 
        return ind2 + 1 
    if (ind2 < 0):
        return ind1 + 1
    
    if (s1[ind1] == s2[ind2]): 
        return 0 + editDistance(ind1 - 1, ind2 - 1, s1, s2) 
    else: 
        return 1 + min(editDistance(ind1 - 1, ind2 - 1, s1, s2), editDistance(ind1, ind2 - 1, s1, s2), editDistance(ind1 - 1, ind2, s1, s2))
    

def editDist(ind1, ind2, s1, s2, dp): 
    if (ind1 < 0): 
        return ind2 + 1 
    if (ind2 < 0): 
        return ind1 + 1 
    if (dp[ind1][ind2] != -1): 
        return dp[ind1][ind2] 
    
    if (s1[ind1] == s2[ind2]): 
        dp[ind1][ind2] = 0 + editDist(ind1 - 1, ind2 - 1, s1, s2, dp)
        return dp[ind1][ind2] 
    else: 
        dp[ind1][ind2] =  1 + min(editDist(ind1 - 1, ind2 - 1, s1, s2, dp), editDist(ind1 - 1, ind2, s1, s2, dp), editDist(ind1,ind2 - 1, s1, s2, dp)) 
        return dp[ind1][ind2] 

def editMemo(s1, s2): 
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))] 
    return editDist(len(s1) - 1, len(s2) - 1, s1, s2, dp)

def editDistTabulation(s1, s2): 
    ind1 = len(s1) 
    ind2 = len(s2) 

    dp = [[0 for _ in range(ind2 + 1)] for _ in range(ind1 + 1)] 
    for i in range(ind1 + 1): 
        dp[i][0] = i 

    for j in range(ind2 + 1): 
        dp[0][j] = j   

    for i in range(1, ind1 + 1): 
        for j in range(1, ind2 + 1): 
            if (s1[i - 1] == s2[j - 1]): 
                dp[i][j] = dp[i - 1][j - 1] 
            else: 
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) 
    
    return dp[ind1][ind2] 




s1 = "horse"
s2 = "ros"
    # Calculate and print the minimum number of operations required
print("The minimum number of operations required is:", editDistTabulation(s1, s2))