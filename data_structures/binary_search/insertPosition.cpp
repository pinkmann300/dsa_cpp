#include <iostream>
#include <cmath>

using namespace std;

int searchPosition(vector<int> &arr1, int targetVal);

int main()
{
    vector<int> arr = {1, 2, 4, 7};
    int x = 6;
    int ind = searchPosition(arr, x);
    cout << "The index is: " << ind << "\n";
    return 0;
}

int searchPosition(vector<int> &arr1, int targetVal)
{
    int low = 0;
    int high = arr1.size() - 1;
    int targetPos = -1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr1[mid] >= targetVal)
        {
            targetPos = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return targetPos;
}