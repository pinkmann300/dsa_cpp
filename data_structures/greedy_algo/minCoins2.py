def minCoins(arr, target): 
    arr.sort(reverse = True) 
    numberOfCoins = 0 
    coinIndex = 0 

    if target <= 0:
        return 0 

    while target > 0 and coinIndex < len(arr): 
        currentDem = arr[coinIndex] 
        if currentDem <= target:
            coinCount = target // currentDem
            target -= (coinCount * currentDem)
            numberOfCoins += coinCount 
        coinIndex += 1 
    return numberOfCoins 


arr = [ 1, 2, 5, 10, 20, 50, 100, 500, 1000 ] 
print(minCoins(arr, 121))

