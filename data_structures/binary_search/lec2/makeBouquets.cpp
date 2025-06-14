// Solution for make bouquets problems.
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

// Problem Statement: You are given 'N’ roses and you are also given an array 'arr'  where 'arr[i]'  denotes that the 'ith' rose will bloom on the 'arr[i]th' day.
// You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet.
// Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses.
// Return -1 if it is not possible.

// Example 1:
// Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
// Result: 12
// Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed.
// So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

// Example 2:
// Input Format: N = 5, arr[] = {1, 10, 3, 10, 2}, m = 3, k = 2
// Result: -1
// Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers.
// But we are given only 5 flowers, so, we cannot make the bouquets.

bool possible(vector<int> &arr1, int k, int m, int days);
int minimumBouquets(vector<int> &arr1, int k, int m);

int main()
{
    vector<int> arr = {7, 7, 7, 7, 13, 11, 12, 7};
    cout << "MIN DAYS " << minimumBouquets(arr, 3, 2) << endl;
    return -1;
}

bool possible(vector<int> &arr1, int k, int m, int days)
{
    int noOfBouquets = 0;
    int count = 0;
    for (int i = 0; i < arr1.size(); i++)
    {
        if (arr1[i] <= days)
        {
            count++;
        }
        else
        {
            noOfBouquets = noOfBouquets + (count / k);
            count = 0;
        }
    }

    noOfBouquets = noOfBouquets + (count / k);
    return (noOfBouquets >= m);
}

int minimumBouquets(vector<int> &arr1, int k, int m)
{
    if (arr1.size() < (m * k))
    {
        return -1;
    }

    int low = *min_element(arr1.begin(), arr1.end());
    cout << low << endl;
    int high = *max_element(arr1.begin(), arr1.end());

    cout << high << endl;
    int minimumDays = 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (possible(arr1, k, m, mid))
        {
            minimumDays = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return low;
}

// Answer range will lie between - [min(arr) , max(arr)]