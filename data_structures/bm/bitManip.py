def nToBin(n):
    if n == 0: 
        return "0"
    revNum = ""
    while n > 1: 
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

print(binToN(111111))