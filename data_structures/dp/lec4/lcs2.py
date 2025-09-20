def longestCSRec(s1, s2, ind1, ind2, count):
    # Base case: if we go out of bounds
    if ind1 < 0 or ind2 < 0:
        return count

    # If characters match, extend the substring
    if s1[ind1] == s2[ind2]:
        count = longestCSRec(s1, s2, ind1 - 1, ind2 - 1, count + 1)

    # Otherwise, reset count but explore both options
    k = longestCSRec(s1, s2, ind1 - 1, ind2, 0)
    r = longestCSRec(s1, s2, ind1, ind2 - 1, 0)

    return max(count, k, r)

def longestCommonSubstringTabulation(s1, s2): 
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] 
    ans = 0 
    for i in range(1, m+1): 
        for j in range(1, n+1):
            if (s1[i - 1] == s2[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1] 
                ans = max(dp[i][j], ans) 
            else: 
                dp[i][j] = 0 
    return ans

print(longestCSRec("asandeepwe", "csandeepa", len("asandeepwe") - 1, len("csandeepa") - 1, 0))



                
