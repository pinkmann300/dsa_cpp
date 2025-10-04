def assignCookies(students, cookie): 
    studentIndex = 0 
    cookieIndex = 0 

    students.sort() 
    cookie.sort() 

    while cookieIndex < len(cookie) and studentIndex < len(students): 
        if (cookie[cookieIndex] >= students[studentIndex]): 
            studentIndex += 1 
        cookieIndex += 1 

    return studentIndex

student = [1, 2, 3]
cookie = [1,2]

print(assignCookies(student, cookie))