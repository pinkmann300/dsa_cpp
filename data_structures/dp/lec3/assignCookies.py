def assignCookies(studentList, cookieList): 
    studentList.sort() 
    cookieList.sort() 

    def helper(studentIndex, cookieIndex): 
        result = 0 
        if (studentIndex >= len(studentList) or cookieIndex >= len(cookieList)): 
            return 0 
        else: 
            if (studentList[studentIndex] <= cookieList[cookieIndex]): 
                result = max(result, 1 + helper(studentIndex + 1, cookieIndex + 1))
            result = max(result, helper(studentIndex, cookieIndex + 1))
        return result 
    return helper(0,0)

student = [1, 2, 3]
cookie = [1, 1]

n = assignCookies(student, cookie) 
print(n) 
