#include <iostream>
#include <cmath>

using namespace std;

bool twoSum(vector<int> &data1, int targetSum);
vector<int> twoSumVar2(vector<int> &data1, int targetSum);
void printArray(vector<int> &data1);

int main()
{
    vector<int> data1 = {2, 6, 5, 8, 11};
    vector<int> answer = twoSumVar2(data1, 15);
    printArray(answer);

    vector<int> answer2 = twoSumVar2(data1, 14);
    printArray(answer2);
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

void printArray(vector<int> &data1)
{
    for (int k : data1)
    {
        cout << k << ", ";
    }

    cout << "\n";
}