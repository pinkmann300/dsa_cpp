#Print all numbers from N till 1. 

def printNto1(n): 
    if (n == 1): 
        print(n) 
    else: 
        print(n) 
        printNto1(n - 1)


def print1ToN(n): 
    if (n == 1): 
        print(1)
    else: 
        print1ToN(n - 1) 
        print(n)

def product1toN(n): 
    if (n == 0): 
        return 1 
    else: 
        k = product1toN(n - 1)
        return n * k 
    

def sumOf1ToN(n): 
    if (n == 1): 
        return 1 
    else: 
        return n + sumOf1ToN(n - 1)
    

def sumOfDigits(n): 
    if (n < 10): 
        return n 
    else: 
        remainder = n % 10 
        return remainder + sumOfDigits(n // 10)
    
def productOfDigits(n): 
    if (n < 10): 
        return n 
    else: 
        return (n % 10) * productOfDigits(n // 10)
    

def countZeros(n, count): 
    if (n < 10): 
        if (n == 0): 
            return count + 1 
        else: 
            return count 
    else: 
        if (n % 10 == 0): 
            return countZeros(n // 10, count + 1) 
        else: 
            return countZeros(n // 10, count)
        

def countStepsToZero(n, count): 
    if (n == 0): 
        return count
    else: 
        if (n % 2 == 0): 
            return countStepsToZero(n // 2, count + 1) 
        else: 
            return countStepsToZero(n - 1, count + 1) 

def palindromeCheck(string1): 
    left = 0 
    right = len(string1) - 1
    while (left <= right): 
        if (string1[left] != string1[right]): 
            return False
        else: 
            left += 1 
            right -= 1 
    return True


print(palindromeCheck("sas"))