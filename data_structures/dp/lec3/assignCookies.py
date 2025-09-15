def assignCookies(studentList, cookieList): 
    studentList.sort() 
    cookieList.sort() 
    return assignCookiesRec(studentList, cookieList, 0, 0) 


def assignCookiesRec(studentList, cookieList, studentIndex, cookieIndex): 
    if cookieIndex >= len(cookieList): 
        return 0
    if studentIndex >= len(studentList): 
        return 0
    greed = 0 
    if (studentList[studentIndex] <= cookieList[cookieIndex]): 
        greed = 1 + assignCookiesRec(studentList, cookieList, studentIndex + 1, cookieIndex + 1) 
    notTaken = 0 + assignCookiesRec(studentList, cookieList, studentIndex, cookieIndex + 1) 

    return max(notTaken, greed) 

def assignMemoization(studentList, cookieList, studentIndex, cookieIndex, dp): 
    if cookieIndex >= len(cookieList): 
        return 0
    if studentIndex >= len(studentList): 
        return 0
    if dp[cookieIndex][studentIndex] != -1: 
        return dp[cookieIndex][studentIndex] 
    greed = 0 
    if (studentList[studentIndex] <= cookieList[cookieIndex]): 
        greed = max(greed, 1 + assignCookiesRec(studentList, cookieList, studentIndex + 1, cookieIndex + 1)) 
    notTaken = max(greed, 0 + assignCookiesRec(studentList, cookieList, studentIndex, cookieIndex + 1))
    dp[cookieIndex][studentIndex] = notTaken 
    return dp[cookieIndex][studentIndex] 

def assignTab(student, cookie, studentIndex, cookieIndex): 
    dp = [[0 for _ in range(cookieIndex + 1)] for _ in range(studentIndex + 1)] 
    for i in range(studentIndex, -1, -1): 
        for j in range(cookieIndex - 1, -1, -1): 
            skip = dp[i][j + 1]
            # Take current cookie if it satisfies student's greed
            take = 0
            if cookie[j] >= student[i]:
                take = 1 + dp[i + 1][j + 1]
                # Take the best of both choices
            dp[i][j] = max(skip, take)

        return dp[0][0]





student = [1, 2, 3]
cookie = [1, 1]

n = assignCookies(student, cookie) 
print(n) 
