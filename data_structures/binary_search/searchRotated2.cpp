#include <iostream>
#include <cmath>

using namespace std;

bool searchRotated2(vector<int> arr2, int target);

int main()
{
    vector<int> arr = {7, 8, 1, 2, 3, 3, 3, 4, 5, 6};
    int k = 3;
    bool ans = searchRotated2(arr, k);
    if (!ans)
        cout << "Target is not present.\n";
    else
        cout << "Target is present in the array.\n";
    return 0;
}

bool searchRotated2(vector<int> arr2, int target)
{

    int length = arr2.size();
    int low = 0;
    int high = length - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;

        // Case 1: Mid value is equal to search value.
        if (arr2[mid] == target)
        {
            return true;
        }

        // Case 2: Mid value is not equal to search value
        // Subcase 1 :

        if ((arr2[mid] == arr2[low]) && arr2[mid] == arr2[high])
        {
            low = low + 1;
            high = high - 1;
            continue;
        }

        // Left part is sorted.
        if ((arr2[mid] >= arr2[low]))
        {
            if (arr2[low] <= target && arr2[mid] >= target)
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
            if (target >= arr2[mid] && arr2[high] >= target)
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }
    }
    // Element unfound return statement.
    return false;
}