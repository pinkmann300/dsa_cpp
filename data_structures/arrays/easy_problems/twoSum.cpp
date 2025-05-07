#include <iostream>
#include <cmath>

using namespace std;

bool twoSum(vector<int> &data1, int targetSum);

int main()
{
    vector<int> data1 = {2, 6, 5, 8, 11};
    cout << (twoSum(data1, 15) ? "YES" : "NO") << endl;
    return 0;
}

// Brute force method.
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