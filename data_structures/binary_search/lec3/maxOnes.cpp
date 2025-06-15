#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

// Problem Statement: You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. All the rows are sorted in ascending order.
// Your task is to find the index of the row with the maximum number of ones.
// Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1.

// Example 1:
// Input Format: n = 3, m = 3,
// mat[] =
// 1 1 1
// 0 0 1
// 0 0 0
// Result: 0
// Explanation: The row with the maximum number of ones is 0 (0 - indexed).

// Example 2:
// Input Format: n = 2, m = 2 ,
// mat[] =
// 0 0
// 0 0
// Result: -1
// Explanation:  The matrix does not contain any 1. So, -1 is the answer.

int maximumOnes(vector<vector<int>> &matrix);
int firstOccurrence(vector<int> &arr, int n);
int lastOccurrence(vector<int> &arr, int n);

int main()
{
    vector<vector<int>> matrix = {{1, 1, 1}, {0, 0, 1}, {0, 0, 0}};
    cout << "The row with maximum no. of 1's is: " << maximumOnes(matrix) << '\n';
    return 0;
}

int firstOccurrence(vector<int> &arr, int n)
{
    int low = 0;
    int high = arr.size() - 1;

    int firstInd = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] == n)
        {
            firstInd = mid;
            high = mid - 1;
        }

        else if (arr[mid] > n)
        {
            high = mid - 1;
        }

        else
        {
            low = mid + 1;
        }
    }

    return firstInd;
}

int lastOccurrence(vector<int> &arr, int n)
{
    int low = 0;
    int high = arr.size() - 1;
    int lastInd = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] == n)
        {
            lastInd = mid;
            low = mid + 1;
        }
        else if (arr[mid] > n)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return lastInd;
}

int maximumOnes(vector<vector<int>> &matrix)
{
    int maxOnes = -1;
    int ansIndex = -1;

    for (int i = 0; i < matrix.size(); i++)
    {
        if ((lastOccurrence(matrix[i], 1) - firstOccurrence(matrix[i], 1)) + 1 > maxOnes)
        {
            maxOnes = (lastOccurrence(matrix[i], 1) - firstOccurrence(matrix[i], 1)) + 1;
            ansIndex = i;
        }
    }

    return ansIndex;
}