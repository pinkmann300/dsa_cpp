
#include <iostream>
#include <cmath>
#include <numeric>
#include <algorithm>

using namespace std;

// Given an array nums which contains n non-negative integers, split it into k non-empty continuous subarrays (exactly k groups).
// Minimize the largest sum among these subarrays.

// Return the minimal possible largest sum among the k splits.

// Lower bound - max(Arr);
// Upper bound - sum(Arr);

int countGroups(vector<int> &arr1, int sumLimit);

int minimisedSum(vector<int> &arr1, int k)
{
    int low = *max_element(arr1.begin(), arr1.end());
    int high = accumulate(arr1.begin(), arr1.end(), 0);
    int minimisedAns = -1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (countGroups(arr1, mid) > k)
        {
            low = mid + 1;
        }
        else
        {

            high = mid - 1;
            minimisedAns = mid;
        }
    }

    return minimisedAns;  
}

int countGroups(vector<int> &arr1, int sumLimit)
{
    int groups = 1;
    int sum = 0;
    for (int i = 0; i < arr1.size(); i++)
    {
        if (sum + arr1[i] <= sumLimit)
        {
            sum += arr1[i];
        }
        else
        {
            groups++;
            sum = arr1[i];
        }
    }

    return groups;
}