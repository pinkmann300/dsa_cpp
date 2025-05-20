#include <iostream>
#include <cmath>

using namespace std;

int maxSubArrayBrute(vector<int> &data1);
int maxSubArrayBetter(vector<int> &data1);
int maxSubArrayOptimal(vector<int> &data1);
int maxSubArrayOptimal2(vector<int> &data1);

int main()
{
    vector<int> data1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int maxSum = maxSubArrayOptimal(data1);
    cout << "The maximum subarray sum is: " << maxSum << endl;
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

int maxSubArrayBetter(vector<int> &data1)
{
    int length = data1.size();

    int maxSum = 0;

    for (int i = 0; i < length; i++)
    {
        int sum = 0;
        for (int j = i; j < length; j++)
        {
            sum += data1[j];
            maxSum = max(sum, maxSum);
        }
    }

    return maxSum;
}

int maxSubArrayOptimal(vector<int> &data1)
{
    int length = data1.size(); // Length of the array.
    int sum = 0;
    int maximum = 0;
    for (int i = 0; i < data1.size(); i++)
    {
        sum += data1[i];
        if (sum > maximum)
        {
            maximum = sum;
        }

        if (sum < 0)
        {
            sum = 0;
        }
    }

    return maximum;
}

int maxSubArrayOptimal2(vector<int> &data1)
{
    int length = data1.size(); // Length of the array.
    int sum = 0;
    int maximum = 0;
    int startAns = 0;
    int endAns = 0;
    int start = 0;

    for (int i = 0; i < data1.size(); i++)
    {

        if (sum == 0)
        {
            start = i;
        }

        sum += data1[i];

        if (sum > maximum)
        {
            maximum = sum;
            startAns = start;
            endAns = i;
        }

        if (sum < 0)
        {
            sum = 0;
        }
    }

    return maximum;
}