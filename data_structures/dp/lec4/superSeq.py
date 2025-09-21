def shortestSuperSeq(s1, s2):
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


    colIndex = len(s1)   
    rowIndex = len(s2) 
    
    superSequence = ""

    while (rowIndex > 0 and colIndex > 0): 
        if (s1[rowIndex - 1] == s2[colIndex - 1]): 
            superSequence = s1[rowIndex - 1] + superSequence
            rowIndex = rowIndex - 1 
            colIndex = colIndex - 1 
        else: 
            if dp[rowIndex - 1][colIndex] > dp[rowIndex][colIndex - 1]: 
                superSequence = s1[rowIndex - 1] + superSequence 
                rowIndex = rowIndex - 1 
            else: 
                superSequence = s2[colIndex - 1] + superSequence
                colIndex = colIndex - 1 
    
    while (rowIndex > 0): 
        superSequence = s1[rowIndex - 1] + superSequence 
        rowIndex = rowIndex - 1 
    
    while (colIndex > 0):
        superSequence = s2[colIndex - 1] + superSequence 
        colIndex = colIndex - 1 

    return superSequence


print(shortestSuperSeq("brute", "groot"))