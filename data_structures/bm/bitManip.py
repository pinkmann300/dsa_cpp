def nToBin(n):
    if n == 0: 
        return "0"
    revNum = ""
    while n > 0: 
        revNum = str((n % 2)) + revNum
        n = n // 2 
    return revNum 

def binToN(n): 
    power2 = 0 
    decimal = 0 
    while n > 0:
        decimal = decimal + ((2 ** power2) * (n % 10)) 
        power2 += 1 
        n = n // 10
    return decimal 

def numberPow2(n): 
    if n == 0: 
        return True 
    else: 
        return (n & (n - 1) == 0) 


def swap2(a,b): 
    a = a ^ b 
    b = a ^ b
    a = a ^ b

    return a, b

def oddOccurence(arr): 
    finalXor = 0 
    for i in arr: 
        finalXor = finalXor ^ i 
    return (finalXor) 

def xorLR(l, r): 
    finalXor = l 
    for i in range(l, r + 1): 
        finalXor = finalXor ^ i 

    return finalXor

print(oddOccurence([2,2,4,4,5]))

