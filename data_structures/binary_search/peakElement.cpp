
#include <iostream>
#include <cmath>

using namespace std;

int findPeakElement(vector<int> &arr, int low, int high)
{
    int n = arr.size(); // Size of array.

    // Edge cases:
    if (n == 1)
        return 0;
    if (arr[0] > arr[1])
        return 0;
    if (arr[n - 1] > arr[n - 2])
        return n - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;

        // If arr[mid] is the peak:
        if (arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1])
            return mid;

        // If we are in the left:
        if (arr[mid] > arr[mid - 1])
        {
            low = mid + 1;
        }

        // If we are in the right:
        // Or, arr[mid] is a common point:
        else if (arr[mid] == arr[mid - 1] && arr[mid] == arr[mid + 1])
        {
            int left = findPeakElement(arr, low, mid);
            int right = findPeakElement(arr, mid + 1, high);
            int ans = max(left, right);
            return ans;
        }
        else
        {
            high = mid - 1;
        }
    }
    // Dummy return statement
    return -1;
}

int main()
{
    vector<int> arr = {1, 2, 3, 7, 8, 5, 1};
    int ans = findPeakElement(arr, 1, arr.size() - 2);
    cout << "The peak is at index: " << ans << "\n";
    return 0;
}