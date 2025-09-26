def lcs(s1, s2, ind1, ind2, count): 
    if (ind1 < 0): 
        return count
    if (ind2 < 0):
        return count
    
    else:
        if (s1[ind1] == s2[ind2]): 
            return  lcs(s1, s2, ind1 - 1, ind2 - 1, count + 1) 
        
        else:
            s1taken = lcs(s1, s2, ind1 - 1, ind2, 0) 
            s2taken = lcs(s1, s2, ind1, ind2 - 1, 0)  

            return max(s1taken, s2taken)
        
s1 = "abcde"
s2 = "abfce"

print(lcs(s1, s2, 4, 4, 0))