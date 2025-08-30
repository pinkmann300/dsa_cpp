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
        
k = "saaandeep" 
print(removeAs(k, ""))