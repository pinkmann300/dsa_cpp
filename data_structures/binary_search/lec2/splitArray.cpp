#include <iostream>
#include <cmath>
#include <numeric>

using namespace std;

// Problem Statement: Given an integer array ‘A’ of size ‘N’ and an integer ‘K'.
// Split the array ‘A’ into ‘K’ non-empty subarrays such that the largest sum of any subarray is minimized.
// Your task is to return the minimized largest sum of the split. A subarray is a contiguous part of the array.

// Example 1:
// Input Format: N = 5, a[] = {1,2,3,4,5}, k = 3
// Result: 6
// Explanation: There are many ways to split the array a[] into k consecutive subarrays.
// The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

// Example 2:
// Input Format: N = 3, a[] = {3,5,1}, k = 3
// Result: 5
// Explanation: There is only one way to split the array a[] into 3 subarrays, i.e., [3], [5], and [1]. The largest sum among these subarrays is 5.

int computeSubarrays(vector<int> &arr, int sumLimit);
int minimizedLargeSum(vector<int> &arr, int partitions);

int main()
{
    vector<int> a = {10, 20, 30, 40};
    int k = 2;
    int ans = minimizedLargeSum(a, k);
    cout << "The answer is: " << ans << "\n";

    return 0;
}

// Observation :
// Answer range will lie between max(arr) and sum(arr);

int computeSubarrays(vector<int> &arr, int sumLimit)
{
    int noOfPartitions = 1;
    int currentSum = 0;

    for (int i = 0; i < arr.size(); i++)
    {
        if (currentSum + arr[i] <= sumLimit)
        {
            currentSum += arr[i];
        }
        else
        {
            noOfPartitions++;
            currentSum = arr[i];
        }
    }

    return noOfPartitions;
}

int minimizedLargeSum(vector<int> &arr, int partitions)
{
    int low = *max_element(arr.begin(), arr.end());
    int high = accumulate(arr.begin(), arr.end(), 0);

    int minimizedMax = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (computeSubarrays(arr, mid) > partitions)
        {
            low = mid + 1;
        }
        else
        {
            minimizedMax = mid;
            high = mid - 1;
        }
    }

    return minimizedMax;
}