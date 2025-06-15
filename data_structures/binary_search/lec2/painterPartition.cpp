#include <iostream>
#include <cmath>
#include <numeric>
#include <algorithm>

using namespace std;

// Problem Statement: Given an array/list of length ‘N’, where the array/list represents the boards and each element of the given array/list
// represents the length of each board. Some ‘K’ numbers of painters are available to paint these boards. Consider that each unit of a board
// takes 1 unit of time to paint. You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards
// under the constraint that any painter will only paint the continuous sections of boards.

// Example 1:
// Input Format: N = 4, boards[] = {5, 5, 5, 5}, k = 2
// Result: 10
// Explanation: We can divide the boards into 2 equal-sized partitions, so each painter gets 10 units of the board and the total time taken is 10.

// Example 2:
// Input Format: N = 4, boards[] = {10, 20, 30, 40}, k = 2
// Result: 60
// Explanation: We can divide the first 3 boards for one painter and the last board for the second painter.

int paintersRequired(vector<int> &arr, int time);
int minimizedTime(vector<int> &arr, int noOfPainters);

int main()
{
    vector<int> boards = {10, 20, 30, 40};
    int k = 2;
    int ans = minimizedTime(boards, k);
    cout << "The answer is: " << ans << "\n";
    return 0;
}

// Answer lies in the range max(arr) and sum(arr)
// For each minimum time, we compute the number of painters required and compare it with the
// number of painters available to us at the time.

int paintersRequired(vector<int> &arr, int time1)
{
    int painters = 1;
    int time = 0;

    for (int i = 0; i < arr.size(); i++)
    {
        if (time + arr[i] <= time1)
        {
            time += arr[i];
        }
        else
        {
            painters++;
            time = arr[i];
        }
    }
    return painters;
}

int minimizedTime(vector<int> &arr, int noOfPainters)
{
    int low = *max_element(arr.begin(), arr.end());
    int high = accumulate(arr.begin(), arr.end(), 0);

    int minimizedTime = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (paintersRequired(arr, mid) > noOfPainters)
        {
            low = mid + 1;
        }
        else
        {
            minimizedTime = mid;
            high = mid - 1;
        }
    }

    return minimizedTime;
}