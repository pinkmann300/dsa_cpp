from collections import Counter 

def brute3sum(arr): 
    results = []
    for i in range(0, len(arr)): 
        for k in range(i + 1, len(arr)): 
            for j in range(k + 1, len(arr)): 
                if arr[i] + arr[k] + arr[j] == 0: 
                    results.append([arr[i], arr[k], arr[j]]) 

    return results


def minimumWindowSubstringBrute(s, t): 
    sLen = len(s)
    tLen = len(t) 
    minString = s

    for i in range(0, sLen - tLen + 1): 
        tMap = Counter(t)
        for j in range(i, sLen): 
            if s[j] in tMap and tMap[s[j]] > 0: 
                tMap[s[j]] -= 1 

            allCut = all(v == 0 for v in tMap.values()) 
            
            if allCut: 
                if len(minString) > (j - i + 1): 
                    minString = s[i : j + 1] 
                    break 

    return minString