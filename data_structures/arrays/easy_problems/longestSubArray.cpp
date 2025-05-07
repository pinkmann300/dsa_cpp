#include <iostream>
#include <cmath>

using namespace std;

int longestSubarrayBrute(vector<int> &data1, int targetSum);

int main()
{
    vector<int> data1 = {2, 3, 5};
    cout << longestSubarrayBrute(data1, 5) << endl;

    vector<int> data2 = {2, 3, 5, 1, 9};
    cout << longestSubarrayBrute(data2, 10) << endl;

    return 1;
}

int longestSubarrayBrute(vector<int> &data1, int targetSum)
{
    int maxLen = 0;
    for (int i = 0; i < data1.size(); i++)
    {
        int sum = data1[i];
        for (int j = i + 1; j < data1.size(); j++)
        {
            sum += data1[j];
            if (sum == targetSum)
            {
                int length = j - i + 1;
                maxLen = max(length, maxLen);
            }
        }
    }
    return maxLen;
}
