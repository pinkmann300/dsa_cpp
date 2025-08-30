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
    


# Iterative functions begin here. 
