def minCoins(denominations, target): 
    totalTarget = target 
    totalCoins = 0 

    for i in range(len(denominations) - 1, -1, -1): 
        if (denominations[i] <= totalTarget): 
            coinCount = totalTarget // denominations[i] 
            totalCoins += coinCount 
            totalTarget = totalTarget % denominations[i] 
        
        if (totalTarget == 0): 
            return totalCoins
        


V = 49
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
print(minCoins(coins, V))
        