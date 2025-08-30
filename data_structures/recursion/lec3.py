# Pattern questions 

def tri1(n): 
    if (n == 1): 
        print("*") 
    else: 
        tri1(n - 1)
        print("*" * n, end = "\n")
        

tri1(4)