#include <iostream>
#include <cmath>

using namespace std;

int rotations(vector<int> &data1);

int main()
{
    vector<int> arr = {4, 5, 6, 7, 0, 1, 2, 3};
    int ans = rotations(arr);
    cout << "The array is rotated " << ans << " times.\n";
    return 0;
    return -1;
}

int rotations(vector<int> &arr)
{
    int numberOfRotations = 0;

    int low = 0;
    int high = arr.size() - 1;

    int minElement = INT_MAX;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] >= arr[low])
        {
            if (arr[low] < minElement)
            {
                minElement = arr[low];
                numberOfRotations = low;
            }
            low = mid + 1;
        }
        else
        {
            if (arr[mid] < minElement)
            {
                minElement = arr[mid];
                numberOfRotations = mid;
            }
            high = mid - 1;
        }
    }
    return numberOfRotations;
}