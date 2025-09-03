def f(n, dp): 
    if n <= 1: 
        return n 
    if dp[n] != -1: 
        return dp[n] 
    dp[n] = f(n - 1, dp) + f(n - 2, dp) 
    return dp[n] 

def tab(n): 
    dp = [-1] * (n + 1)
    dp[0] = 0 
    dp[1] = 1 
    count = 2 
    while (count < n + 1): 
        dp[count] = dp[count - 1] + dp[count - 2] 
        count += 1
    return dp[n]


def spaceOptim(n): 
    prev_2 = 0 
    prev_1 = 1
    index = 2 
    while index <= n: 
        current = prev_2 + prev_1 
        prev_2 = prev_1 
        prev_1 = current 
        index += 1 
    return current 


k = spaceOptim(5)
print(k)