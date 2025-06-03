#include <iostream>
#include <cmath>

using namespace std;

int minElement(vector<int> arr1);
// Arr1 consists only of distinct values and is rotated.

int main()
{
    vector<int> arr = {4, 5, 6, 7, 0, 1, 2, 3};
    int ans = minElement(arr);
    cout << "The minimum element is: " << ans << "\n";
    return 0;
    // Main return statement.
}

int minElement(vector<int> arr1)
{
    int low = 0;
    int high = arr1.size() - 1;
    int minEl = INT_MAX;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr1[mid] >= arr1[low])
        {
            minEl = min(arr1[low], minEl);
            low = mid + 1;
        }
        else
        {
            minEl = min(arr1[mid], minEl);
            high = mid - 1;
        }
    }

    return minEl;
}
