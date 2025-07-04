#Check for valid paranthesis
def checkValidParenthesis(string1):
    opening_list = []
    for i in range(0, len(string1)):
        if (string1[i] == '(' or string1[i] == '{' or string1[i] == '['):
            opening_list.append(string1[i])

        else:
            if ((string1[i] == ')' and opening_list.pop() == "(") or (string1[i] == '}' and opening_list.pop() == "{") or (string1[i] == ']' and opening_list.pop() == "[")):
                continue
            else: 
                return False 
        
    return (len(opening_list) == 0)


