def printNto1(n): 
    if (n == 1): 
        print(n) 
    else: 
        print(n) 
        printNto1(n - 1)

    
def print1ToN(n): 
    if (n == 1): 
        print(n) 
    else: 
        print1ToN(n - 1)
        print(n)

def factorialn(n): 
    if n == 0: 
        return 1 
    else: 
        return n * factorialn(n - 1)
    
    #Recurrence relation : f(n) = n * f(n - 1)

def sumTon(n): 
    if n == 0: 
        return 0 
    else: 
        return n + sumTon(n - 1)
    

def sumOfDigits(n): 
    if (n < 10): 
        return n 
    else: 
        unitsPlace = n % 10 
        return unitsPlace + sumOfDigits(n // 10)


def prodOfDigits(n): 
    if (n < 10): 
        return n
    else: 
        unitsPlace = n % 10 
        if unitsPlace == 0: 
            return 0 
        else:
            return unitsPlace * prodOfDigits(n // 10)
        
def revNum(n, val, multiplier): 
    if (n == 0): 
        return val * multiplier
    else: 
        if (n < 0):
            n = -1 * n
            return revNum(n, val, -1)
        else:
            units = n % 10 
            val = (val * 10) + units 
            return revNum(n // 10, val, multiplier)
        

def palindrome(val, s, h): 
    if (s >= h):
        return True 
    else: 
        if (val[s] == val[h]): 
            return palindrome(val, s + 1, h - 1) 
        else: 
            return False 



    

print(revNum(-123, 0, 1))
print(-123 % 10)

print(palindrome("malayala", 0, 7))