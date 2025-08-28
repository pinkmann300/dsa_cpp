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


def linearSearch(list1, target):
    if (len(list1) == 0): 
        return False 
    elif (list1[0] == target):
        return True 
    else:
        return False or linearSearch(list1[1:], target)
    
def iterativeCom(list1): 
    allCombos = []
    for i in range(len(list1)): 
        result = [list1[i]] 
        print(result)
        allCombos.append(result.copy())
        for j in range(i + 1, len(list1)): 
            result.append(list1[j])
            allCombos.append(result.copy()); 
    return allCombos


def subsetPrint(string1, val):
    if (string1 == ""): 
        return [val] if val != '' else []
    else:
        r = subsetPrint(string1[1:], val)
        k = subsetPrint(string1[1:], val + (string1[0])) 
        return (r + k)

def generateBinaryStringsHelper(num1, genVal): 
    if (num1 == 0): 
        print(genVal) 
    else: 
        generateBinaryStringsHelper(num1 - 1, genVal + "0")
        if (len(genVal) == 0) or genVal[-1] != '1':
            generateBinaryStringsHelper(num1 - 1, genVal + "1")

def generateAllBinStrings(num1, genVal): 
    if (num1 == 0): 
        print(genVal) 
    else: 
        generateAllBinStrings(num1 - 1, genVal=genVal + "0") 
        generateAllBinStrings(num1 - 1, genVal=genVal + "1") 

def generateAllBinStringsList(num1, genVal): 
    if (num1 == 0): 
        return [genVal] 
    else: 
        k = generateAllBinStringsList(num1 - 1, genVal=genVal + "0") 
        r = generateAllBinStringsList(num1 - 1, genVal=genVal + "1")

        return (k + r )
    
def subsequences(string1, genVal): 
    if (string1 == ""): 
        return [genVal] if genVal != '' else []
    else: 
        k = subsequences(string1[1:], genVal + string1[0]) 
        r = subsequences(string1[1:], genVal) 
        return (k + r)      
    
def powerSet(numbers, genVal): 
    if (len(numbers) == 0): 
        return [genVal] 
    else:
        k = powerSet(numbers[1:], genVal + [(numbers[0])]) 
        r = powerSet(numbers[1:], genVal) 

        return k + r 
    
def generateParen(num1, genVal): 
    if num1 == 0: 
        return [genVal] 
    else: 
        k = generateParen(num1 - 1, '(' + genVal + ')')
        r = generateParen(num1 - 1,  genVal + '()')
        l = generateParen(num1 - 1, '()' + genVal)

        return (k + r + l)

def pow(x, n): 
    if (n == 0): 
        return 1 
    else: 
        return x * pow(x, n - 1)
    

# def powerRepSq(x, n): 
#     if n == 0: 
#         return 1
#     ans = 1
#     while (n):
#         if (n % 2 == 1): 
#             ans = ans * x 
#         else: 
#             x = x * x 
        

# def recursiveAtoI(string1, genVal): 
#     if (string1 == ""):
#         return genVal 
#     else: 
#         if (string1[-1].numeric()):
#             pass 

#While the function has not finished executing, the function remains in the stack. 
#Once the function has completed execution down to it's last line, it will get popped off
#the stack.
        
#Function calls keep getting pushed into the stack as and when they are called recursively 
# and only gets popped out after the base case is hit.  Once the function gets popped off the stack 
#the flow of program gets returned to where that function was called.  If a function is called again and again 
# it will be treated as a seperate entity on the call stack. Every call takes memory on the stack and since no 
# element is getting popped off, the stack runs out of memory to accomodate and that is when you run into a 
# "stack overflow" error. 
    

def fibo(n): 
    if (n == 0) or (n == 1): 
        return n 
    else: 
        return fibo(n - 1) + fibo(n - 2) 
    

print(fibo(6))