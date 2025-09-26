def bs1(arr): 
    mini = arr[0] 
    maxProfit = 0 

    for i in range(1, len(arr)): 
        currentProfit = arr[i] - mini 
        maxProfit = max(maxProfit, currentProfit) 
        mini = min(mini, arr[i]) 

    return maxProfit


Arr  =[7,1,5,3,6,4] 
print(bs1(Arr))