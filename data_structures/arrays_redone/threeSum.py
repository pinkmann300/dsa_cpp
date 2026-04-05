def brute3sum(arr): 
    results = []
    for i in range(0, len(arr)): 
        for k in range(i + 1, len(arr)): 
            for j in range(k + 1, len(arr)): 
                if arr[i] + arr[k] + arr[j] == 0: 
                    results.append([arr[i], arr[k], arr[j]]) 

    return results

