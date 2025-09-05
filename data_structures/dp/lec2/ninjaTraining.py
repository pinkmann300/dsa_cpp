def ninjaTrainRec(trainingArr, days, last): 
    if (days == 0):
        maximum = 0  
        for i in range(0, 3):
            if (i != last): 
                maximum = max(trainingArr[days][i], maximum) 
        return maximum 
    
    else: 
        maxi = 0 
        for k in range(0, 3):
            activitySum = trainingArr[days][k] + ninjaTrainRec(trainingArr, days - 1, k) 
            maxi = max(maxi, activitySum) 
        return maxi
    

points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]

n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find the maximum points.
print(ninjaTrainRec(points, 2, 3))