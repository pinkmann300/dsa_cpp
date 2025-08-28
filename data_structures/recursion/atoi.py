def atoi(s, val, power): 
    if (s == ""): 
        return val
    else: 
        character = s[-1] 
        if (character.isdigit() and val >= 0):
            number = int(character) 
            val = (number * (10 ** power)) + val
            return atoi(s[:-1], val, power + 1)
        elif (character.isdigit() and val < 0): 
            val = 0 
            power = 0
            number = int(character) 
            val = (number * (10 ** power)) + val
            return atoi(s[:-1], val, power + 1)
        elif (character == " " ): 
            return atoi(s[:-1], val, power) 
        elif (character == "+"): 
            return atoi(s[:-1], val, power) 
        elif (character == "-"): 
            return atoi(s[:-1], val * -1, power)
        else: 
            return atoi(s[:-1], 0, 0)
               
j ="words and 987"
print(atoi(j, 0, 0))