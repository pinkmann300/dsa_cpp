#Solution outline 

# -- Find the previous smaller index 
# -- Find the next smaller index 
# -- Compute width from pse and nse 
# -- Multiply width with height and maintain 
# -- a max area variable to keep it tight.



def nextSmaller(nums1): 
    nseStack = [] 
    nseArr = [-1] * len(nums1) 
    for i in range(len(nums1) - 1, -1, -1): 
        while (nseStack and nums1[nseStack[-1]] >= nums1[i]): 
            nseStack.pop() 
        nseIndex = len(nums1) - 1 if not nseStack else nseStack[-1] - 1 
        nseArr[i] = nseIndex 
        nseStack.append(i) 
    return nseArr


def previousSmaller(nums1): 
    pseStack = [] 
    pseArr = [-1] * len(nums1)
    for i in range(0, len(nums1)):
        while (pseStack and nums1[pseStack[-1]] >= nums1[i]): 
            pseStack.pop() 
        pseIndex = 0 if not pseStack else pseStack[-1] + 1 
        pseArr[i] = pseIndex 
        pseStack.append(i) 
    return pseArr


def largestArea(nums1): 
    maxArea = 0 
    nseArr = nextSmaller(nums1) 
    pseArr = previousSmaller(nums1) 

    print(nseArr) 
    print(pseArr)
    for i in range(len(nums1)): 
        area = ((nseArr[i] - pseArr[i]) + 1) * nums1[i] 
        maxArea = max(maxArea, area)
    return maxArea

if __name__ == "__main__": 
    histogram = [2, 1, 5, 6, 2, 3, 1] 
    area = largestArea(histogram) 
    print(area) 

