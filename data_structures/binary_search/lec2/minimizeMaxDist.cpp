#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>

using namespace std;

long double minimizeMaxDistance(vector<int> &arr, int gasStations);
int countOfGasStations(vector<int> &arr, int dist);

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 4;
    long double ans = minimizeMaxDistance(arr, k);
    cout << "The answer is: " << ans << "\n";
    return 0;
}

// Answer range lies between 0 and the existing maximum distance.
int countOfGasStations(vector<int> &arr, long double dist)
{
    int count = 0;

    for (int i = 1; i < arr.size() - 1; i++)
    {
        int numberInBetween = ((arr[i] - arr[i - 1]) / dist);
        if ((arr[i] - arr[i - 1]) == (dist * numberInBetween))
        {
            numberInBetween--;
        }
        count += numberInBetween;
    }

    return count;
}

long double minimizeMaxDistance(vector<int> &arr, int gasStations)
{
    long double low = 0;
    long double high = 0;

    long double minMax = -1;

    for (int i = 0; i < arr.size() - 1; i++)
    {
        high = max(high, (long double)(arr[i + 1] - arr[i]));
    }

    long double diff = 1e-6;

    while (high - low > diff)
    {
        long double mid = (low + high) / 2.0;
        if (countOfGasStations(arr, mid) > gasStations)
        {
            low = mid;
        }
        else
        {
            high = mid;
        }
    }

    return high;
}