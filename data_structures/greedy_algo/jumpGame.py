# Problem Statement: Given an array where each element represents the maximum number of steps you can jump forward from that element, return true if we can reach the last index starting from the first index. Otherwise, return false.

def frogJump(jumps): 
    max_index = 0 

    for i in range(len(jumps)): 
        if i > max_index: 
            return False 
        else: 
            if (i + jumps[i] == len(jumps) - 1): 
                return True 
            else: 
                max_index = max(i + jumps[i], max)

    return True 
