#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

// Problem Statement: A monkey is given ‘n’ piles of bananas, whereas the 'ith' pile has ‘a[i]’ bananas. An integer ‘h’ is also given,
// which denotes the time (in hours) for all the bananas to be eaten.
// Each hour, the monkey chooses a non-empty pile of bananas and eats ‘k’ bananas.
// If the pile contains less than ‘k’ bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.
// Find the minimum number of bananas ‘k’ to eat per hour so that the monkey can eat all the bananas within ‘h’ hours.

// Example 1:
// Input Format: N = 4, a[] = {7, 15, 6, 3}, h = 8
// Result: 5
// Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.

// Example 2:
// Input Format: N = 5, a[] = {25, 12, 8, 14, 19}, h = 5
// Result: 25
// Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. So, he will take 5 hours to complete all the piles.

int kokoBanana(vector<int> &piles, int hrs);
int hrsToComplete(vector<int> &piles, int eatRate);

int main()
{
    vector<int> v = {7, 15, 6, 3};
    int h = 8;
    int ans = kokoBanana(v, h);
    cout << "Koko should eat atleast " << ans << " bananas/hr.\n";
    return 0;
    return 0;
}

// This will be the first problem solved using the monitor.
// Super excited for this in some sense.

// The minimum can start at 1 and go upto the maximum number of bananas in an hr.

int hrsToComplete(vector<int> &piles, int eatRate)
{
    int totalHrs = 0;
    for (int i = 0; i < piles.size(); i++)
    {
        totalHrs += ceil((double)(piles[i]) / (double)(eatRate));
    }

    return totalHrs;
}

int kokoBanana(vector<int> &piles, int hrs)
{
    int low = 1;
    int high = *max_element(piles.begin(), piles.end());
    int minAmount = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (hrsToComplete(piles, mid) <= hrs)
        {
            minAmount = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return minAmount;

    return 0;
}
