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

def jumpGame(arr): 
    maxIndexReached = 0 
    current_index = 0 

    while maxIndexReached < len(arr) - 1 and current_index <= len(arr) - 1: 
        if current_index > maxIndexReached: 
            return False 
    
        reachableIndex = current_index + arr[current_index] 
        maxIndexReached = max(maxIndexReached, reachableIndex) 
        current_index += 1 

    return True 



    
