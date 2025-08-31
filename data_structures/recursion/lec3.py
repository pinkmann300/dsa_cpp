# Pattern questions 

def tri1(n): 
    if (n == 1): 
        print("*") 
    else: 
        tri1(n - 1)
        print("*" * n, end = "\n")
        
def removeAs(s, genVal): 
    if (s == ""): 
        return genVal 
    else: 
        if (s[0] == 'a'): 
            return removeAs(s[1:], genVal)
        else: 
            return removeAs(s[1:], genVal + s[0])
        
def subset(arr, genVal): 
    if (len(arr) == 0): 
        return [genVal] if genVal is not None else [] 
    else: 
        k = subset(arr[1:], genVal) 
        r = subset(arr[1:], genVal + [arr[0]])

        return k + r
    
def subsequences(s, genVal): 
    if (len(s) == 0):
        if genVal is not None:  
            print(genVal, end=",")
    else: 
        k = subsequences(s[1:], genVal + s[0]) 
        r = subsequences(s[1:], genVal) 

        print(k, end=",") if k is not None else ""
        print(r, end=",") if r is not None else ""

def subsequencesSet(s, genVal): 
    if (len(s) == 0): 
        if genVal is not None: 
            return [genVal] 
    else: 
        k = subsequencesSet(s[1:], genVal + s[0])
        r = subsequencesSet(s[1:], genVal) 
    
        return k + r 
    
def generateSubsets(arr, genVal): 
    if (len(arr) == 0): 
        if genVal is not None or len(genVal) != 0:  
            return [genVal] 
    else: 
        k = generateSubsets(arr[1:], genVal + [arr[0]]) 
        r = generateSubsets(arr[1:], genVal)

        return k + r
    
def generateParenthesis(genVal, open, close): 
    if (close == 0): 
        return [genVal] 
    else: 
        if (open == close): 
            return generateParenthesis(genVal + '(', open - 1, close)
        
        if (open < close and open > 0): 
            k = generateParenthesis(genVal + '(', open - 1 , close)
            r = generateParenthesis(genVal + ')', open, close - 1)
            return k + r 
        elif (open == 0): 
            return generateParenthesis(genVal + ')', open, close - 1)
    
def countSubsequences(arr, target, genVal, count): 
    if (len(arr) == 0): 
        if (sum(genVal) == target):
            return count + 1
        else: 
            return count
    else: 
        k = countSubsequences(arr[1:], target, genVal + [arr[0]], count)
        r = countSubsequences(arr[1:], target, genVal, count)

        return k + r 

def checkSubsequences(arr, target, genVal, count): 
    if (len(arr) == 0): 
        if (sum(genVal) == target):
            return True
        else: 
            return False
    else: 
        k = checkSubsequences(arr[1:], target, genVal + [arr[0]], count)
        r = checkSubsequences(arr[1:], target, genVal, count)

        return (k or r)

def letterCombinations(digits,genVal):
        map1 = {'2' : ["a", "b", "c"], 
               '3' : ["d", "e", "f"],
               '4' : ["g", "h", "i"], 
               '5' : ["j", "k", "l"], 
               '6' : ["m", "n", "o"], 
               '7' : ["p", "q", "r", "s"], 
               '8' : ["t", "u", "v"],
               '9' : ["w", "x", "y", "z"]} 

        if (len(digits) == 0): 
            if len(genVal) > 0:
                return [genVal]
            else: 
                return []
        else: 
            if (digits[0] == '7' or digits[0] == '9'): 
                k = letterCombinations(digits[1:], genVal + map1[digits[0]][0]) 
                r = letterCombinations(digits[1:], genVal + map1[digits[0]][1])
                n = letterCombinations(digits[1:], genVal + map1[digits[0]][2])
                w = letterCombinations(digits[1:], genVal + map1[digits[0]][3])
                return k + r + n + w 
            else: 
                k = letterCombinations(digits[1:], genVal + map1[digits[0]][0]) 
                r = letterCombinations(digits[1:], genVal + map1[digits[0]][1])
                n = letterCombinations(digits[1:], genVal + map1[digits[0]][2])

                return k + r + n 

def subsetGenIterative(arr): 
    subsets = [] 
    subsets.append([]) 
    for i in arr:
        for j in range(len(subsets)):
            newSubset = subsets[j] + [i]
            subsets.append(newSubset)
    return subsets 

            
k = subsetGenIterative([1,2,3,4,5,6,7])