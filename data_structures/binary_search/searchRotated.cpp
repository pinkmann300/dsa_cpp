#include <iostream>
#include <cmath>

using namespace std;

int searchRotated(vector<int> &data1, int target);

int main()
{
    vector<int> arr = {7, 8, 9, 1, 2, 3, 4, 5, 6};
    cout << searchRotated(arr, 9) << endl;
    return -1;
}

int searchRotated(vector<int> &data1, int target)
{
    int low = 0;
    int high = data1.size() - 1;

    int ans = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (data1[mid] == target)
        {
            return mid;
        }

        if (data1[mid] >= data1[low])
        {
            if (data1[mid] >= target && data1[low] <= target)
            {
                high = mid - 1;
            }
            else
            {
                low = mid + 1;
            }
        }
        else
        {
            if (data1[mid] <= target && data1[high] >= target)
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }
    }

    return ans;
}
