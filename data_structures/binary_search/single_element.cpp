#include <iostream>
#include <cmath>

using namespace std;

int singleElem(vector<int> &arr1);

int main()
{
    vector<int> arr = {1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6};
    int ans = singleElem(arr);
    cout << "The single element is: " << ans << "\n";

    return -1;
}

int singleElem(vector<int> &arr1)
{
    int length = arr1.size();

    if (length == 1)
    {
        return arr1[0];
    }

    if (arr1[length - 1] != arr1[length - 2])
    {
        return arr1[length - 1];
    }

    if (arr1[0] != arr1[1])
    {
        return arr1[0];
    }

    int low = 1;
    int high = length - 2;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr1[mid] != arr1[mid - 1] && arr1[mid] != arr1[mid + 1])
        {
            return arr1[mid];
        }

        else
        {
            if (((mid % 2 == 0) && (arr1[mid] == arr1[mid + 1])) || ((mid % 2 == 1) && (arr1[mid] == arr1[mid - 1])))
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }
    }

    return -1;
}