def reverseWords(s1): 
    finalOutput = "" 
    word = ""

    for i in range(0, len(s1)): 
        if (s1[i] == " " or i == len(s1) - 1): 
            if (i == (len(s1) - 1) and s1[i] != " "): 
                finalOutput = (word + s1[i]) + finalOutput
                word = ""
            else: 
                finalOutput = (" " + word) + finalOutput
                word = ""

        else: 
            word += s1[i] 

    return finalOutput



def reverseWords2(s1): 
    finalOutput = "" 
    index = 0 
    while index < len(s1): 
        word = "" 
        while index < len(s1) and  s1[index] != " ":
            word += s1[index]
            index = index + 1 

        finalOutput = " " + word + finalOutput
        index = index + 1
    return finalOutput 

testString = "This is decent"
print(reverseWords2(testString))
