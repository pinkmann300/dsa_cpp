#include <iostream>
#include <cmath>
#include <map>

using namespace std;

bool twoSum(vector<int> &data1, int targetSum);
vector<int> twoSumVar2(vector<int> &data1, int targetSum);
bool twoSumHashBool(vector<int> &data1, int targetSum);
vector<int> twoSumHashVector(vector<int> &data1, int targetSum);
bool twoSumTwoPointer(vector<int> &dat1, int targetSum);
vector<int> twoSumTwoPointerVec(vector<int> &data1, int targetSum);

void printArray(vector<int> &data1);

int main()
{
    vector<int> data1 = {2, 5, 6, 8, 11};
    vector<int> answer = twoSumVar2(data1, 15);
    printArray(answer);

    vector<int> answer2 = twoSumVar2(data1, 14);
    bool bool_ans = twoSumTwoPointer(data1, 20);
    vector<int> new_ans = twoSumTwoPointerVec(data1, 14);

    cout << (bool_ans ? "YES" : "NO") << endl;
    printArray(new_ans);
    return 0;
}

// Brute force method.
// Variant 1
bool twoSum(vector<int> &data1, int targetSum)
{
    int length = data1.size(); // Length of the array.
    bool pairExists = false;
    for (int i = 0; i < length; i++)
    {
        int remainder = targetSum - data1[i];
        for (int j = i + 1; j < length; j++)
        {
            if (data1[j] == remainder)
            {
                pairExists = true;
                return pairExists;
                break;
            }
        }
    }

    return false;
}

// Brute Force
// Variant 2
vector<int> twoSumVar2(vector<int> &data1, int targetSum)
{
    int length = data1.size();
    vector<int> answer = {-1, -1};
    for (int i = 0; i < length; i++)
    {
        int remainder = targetSum - data1[i];
        for (int j = i + 1; j < length; j++)
        {
            if (data1[j] == remainder)
            {
                answer[0] = i;
                answer[1] = j;
            }
        }
    }
    return answer;
}

bool twoSumHashBool(vector<int> &data1, int targetSum)
{
    map<int, int> map1;
    int length = data1.size();
    bool found = false;

    for (int i = 0; i < length; i++)
    {
        int remainder = targetSum - data1[i];
        if (map1.find(remainder) != map1.end())
        {
            found = true;
            break;
        }
        else
        {
            map1[data1[i]] = i;
        }
    }

    return found;
}

vector<int> twoSumHashVector(vector<int> &data1, int targetSum)
{
    map<int, int> map1;
    int length = data1.size();
    vector<int> result = {-1, -1};
    for (int i = 0; i < length; i++)
    {
        int difference = targetSum - data1[i];
        if (map1.find(difference) != map1.end())
        {
            result[0] = (map1.find(difference))->second;
            result[1] = i;
            break;
        }
        else
        {
            map1[data1[i]] = i;
        }
    }

    return result;
}

bool twoSumTwoPointer(vector<int> &data1, int targetSum)
{
    int length = data1.size();
    bool found = false;
    int left = 0;
    int right = length - 1;

    while (left < right)
    {
        if (data1[left] + data1[right] > targetSum)
        {
            right--;
        }
        else if (data1[left] + data1[right] < targetSum)
        {
            left--;
        }
        else if (data1[left] + data1[right] == targetSum)
        {
            found = true;
            break;
        }
    }

    return found;
}

vector<int> twoSumTwoPointerVec(vector<int> &data1, int targetSum)
{
    vector<int> result = {-1, -1};
    int length = data1.size();
    int left = 0;
    int right = length - 1;
    while (left < right)
    {
        if (data1[left] + data1[right] > targetSum)
        {
            right--;
        }
        else if (data1[left] + data1[right] < targetSum)
        {
            left++;
        }
        else if (data1[left] + data1[right] == targetSum)
        {
            result[0] = left;
            result[1] = right;
            break;
        }
    }

    return result;
}

void printArray(vector<int> &data1)
{
    for (int k : data1)
    {
        cout << k << ", ";
    }

    cout << "\n";
}