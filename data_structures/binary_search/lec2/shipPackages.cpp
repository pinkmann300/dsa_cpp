#include <iostream>
#include <cmath>
#include <algorithm>

#include <numeric>
using namespace std;

// Problem Statement : You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another.
// The packages must be shipped within 'd' days.
// The weights of the packages are given in an array 'of weights'.
// The packages are loaded on the conveyor belts every day in the same order as they appear in the array.
// The loaded weights must not exceed the maximum weight capacity of the ship.
// Find out the least-weight capacity so that you can ship all the packages within 'd' days.

// Example 1:
// Input Format: N = 5, weights[] = {5,4,5,2,3,4,5,6}, d = 5
// Result: 9
// Explanation: If the ship capacity is 9, the shipment will be done in the following manner:
// Day         Weights            Total
// 1        -       5, 4          -        9
// 2        -       5, 2          -        7
// 3        -       3, 4          -        7
// 4        -       5              -        5
// 5        -       6              -        6
// So, the least capacity should be 9.

// Example 2:

// Input Format: N = 10, weights[] = {1,2,3,4,5,6,7,8,9,10}, d = 1
// Result: 55
// Explanation: We have to ship all the goods in a single day. So, the weight capacity should be the summation of all the weights i.e. 55.

int calculateDays(vector<int> weights, int weightLimit);
int leastWeight(vector<int> weights, int days);

int main()
{
    vector<int> weights = {5, 4, 5, 2, 3, 4, 5, 6};
    int d = 5;
    int ans = leastWeight(weights, d);
    cout << "The minimum capacity should be: " << ans << "\n";
    return 0;
}

// Range lies between max(Arr) and sum of all weights in the array.
int calculateDays(vector<int> weights, int weightLimit)
{
    int days = 1;
    int weight = 0;
    for (int i = 0; i < weights.size(); i++)
    {
        if (weight + weights[i] > weightLimit)
        {
            days++;
            weight = weights[i];
        }
        else
        {
            weight += weights[i];
        }
    }

    return days;
}

int leastWeight(vector<int> weights, int days)
{
    int low = *max_element(weights.begin(), weights.end());
    int high = accumulate(weights.begin(), weights.end(), 0);
    int minDays = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (calculateDays(weights, mid) <= days)
        {
            minDays = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return minDays;
}