#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

bool canWePlaceCows(vector<int> &arr, int k, int dist);
int aggressiveCows(vector<int> &arr, int k);

int main()
{

    vector<int> stalls = {0, 3, 4, 7, 10, 9};
    int k = 4;
    int ans = aggressiveCows(stalls, k);
    cout << "The maximum possible minimum distance is: " << ans << "\n";
    return 0;
}

bool canWePlaceCows(vector<int> &arr, int k, int dist)
{
    int count = 1;
    int last = arr[0];
    int length = arr.size();

    for (int i = 1; i < length; i++)
    {
        if (arr[i] - last >= dist)
        {
            last = arr[i];
            count++;
        }

        if (count >= k)
        {
            return true;
        }
    }
    return false;
}

int aggressiveCows(vector<int> &arr, int k)
{

    int ans = -1;
    sort(arr.begin(), arr.end());
    int high = arr[arr.size() - 1];
    int low = 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (canWePlaceCows(arr, k, mid))
        {
            ans = low;
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return ans;
}