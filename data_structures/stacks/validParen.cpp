#include <iostream>
#include <cmath>
#include <stack>

using namespace std;

bool checkParenthesis(string s)
{
    stack<char> charStack;
    for (int i = 0; i < s.size(); i++)
    {
        if ((s[i] == "(") || (s[i] == "{") || (s[i] == "["))
        {
            charStack.push(s[i]);
        }
        else
        {
            if (charStack.empty())
            {
                return false;
            }

            char topChar = charStack.top();
            charStack.pop();

            if ((topChar == '{' && s[i] == '}') || (topChar == '(' && s[i] == ')') || (topChar == '[' && s[i] == ']'))
            {
                continue;
            }
            else
            {
                return false;
            }
        }
    }

    return (charStack.empty());
}

int main()
{
    return 0;
}