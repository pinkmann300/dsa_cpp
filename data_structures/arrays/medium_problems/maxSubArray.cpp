#include <iostream>
#include <cmath>

using namespace std;

int maxSubArrayBrute(vector<int> &data1);
int maxSubArrayOptimal(vector<int> &data1);

int main()
{
    vector<int> data1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int maxSum = maxSubArrayBrute(data1);
    cout << "The maximum subarray sum is: " << maxSum << endl;
    cout << "LONG_MIN" << LONG_MIN << endl; 
    return -1;
}

int maxSubArrayBrute(vector<int> &data1)
{
    int length = data1.size();
    int maxSum = 0;

    for (int i = 0; i < length; i++)
    {
        int startingIndex = i;

        for (int j = i; j < length; j++)
        {
            int sum = 0;

            for (int k = i; k <= j; k++)
            {
                sum += data1[k];
            }

            maxSum = max(sum, maxSum);
        }
    }

    return maxSum;
}