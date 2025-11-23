def checkRotation(string1, rotation1): 
    
    if (len(rotation1) != len(string1)): 
        return False 
    
    checkingString = rotation1 + rotation1
    windowSize = len(string1)

    for startingIndex in range(len(string1)): 
        if checkingString[startingIndex: startingIndex + windowSize] == string1: 
            return True 
        
    return False 

s = "rotation"
goal = "tionroa"

print(checkRotation(s, goal))

