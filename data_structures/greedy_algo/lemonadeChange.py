def lemonadeChange(bills): 
    dollar_5 = 0 
    dollar_10 = 0 

    for i in range(0, len(bills)): 
        if (bills[i] == 5): 
            dollar_5 += 1

        if (bills[i] == 10): 
            if dollar_5: 
                dollar_5 -= 1 
                dollar_10 += 1 
            else: 
                return False 
            
        if (bills[i] == 20): 
            if dollar_10 and dollar_5: 
                dollar_10 -= 1 
                dollar_5 -= 1 

            elif dollar_5 >= 3: 
                dollar_5 -= 3 
            
            else: 
                return False 
    
    return True 




bills = [5, 5, 5, 10, 20]
print("Queues of customers:", end=" ")
ans = lemonadeChange(bills)
if ans:
    print("It is possible to provide change for all customers.")
else:
    print("It is not possible to provide change for all customers.")
