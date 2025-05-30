#include <iostream>
#include <cmath>

using namespace std;

int firstOccurence(vector<int> &arr1, int target);
int main()
{
    vector<int> v = {3, 4, 13, 13, 13, 20, 40};
    cout << firstOccurence(v, 21) << endl;
    return -1;
}

int firstOccurence(vector<int> &arr1, int target)
{
    int low = 0;
    int high = arr1.size() - 1;
    int ind = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr1[mid] == target)
        {
            high = mid - 1;
            ind = mid;
        }
        else if (arr1[mid] > target)
        {
            high = mid - 1;
        }
        else if (arr1[mid] < target)
        {
            low = mid + 1;
        }
    }

    return ind;
}