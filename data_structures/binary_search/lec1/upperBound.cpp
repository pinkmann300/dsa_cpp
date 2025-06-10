#include <iostream>
#include <cmath>

using namespace std;

// Upper bound implementation will go here.

int upperBound(vector<int> arr, int targetVal);

int main()
{
    vector<int> arr1 = {1, 2, 2, 3};
    cout << upperBound(arr1, 2) << endl;
    return -1;
}

int upperBound(vector<int> arr, int targetVal)
{
    int upperBound = -1;
    int mid = -1;
    int low = 0;
    int high = arr.size() - 1;
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (arr[mid] > targetVal)
        {
            upperBound = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return upperBound;
}