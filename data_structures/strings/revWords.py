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

        if index < len(s1) and s1[index - 1] != " ": 
            finalOutput = " " + word + finalOutput
        else: 
            finalOutput = word + finalOutput

        index = index + 1
    return finalOutput 

def lcprefix(words): 
    words_sorted = sorted(words) 
    right = len(words_sorted) - 1 
    left = 0 

    commonPrefix = "" 

    for i in range(0, len(words_sorted[0])): 
        if (words_sorted[left][i] != words_sorted[right][i]): 
            break 
        commonPrefix += words_sorted[left][i]

    return commonPrefix


testString = "This is decent   "
testString2 = ["flower", "flow", "flight"] 
print(lcprefix(testString2))


