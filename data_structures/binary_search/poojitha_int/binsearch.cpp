#include <iostream>
#include <cmath>

using namespace std;

int binSearch(vector<int> &arr, int target);
int newSpot(vector<int> &arr, int target);

int searchInsert(vector<int> &arr, int x)
{
    int n = arr.size(); // size of the array
    int low = 0, high = n - 1;
    int ans = n;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        // maybe an answer
        if (arr[mid] >= x)
        {
            ans = mid;
            // look for smaller index on the left
            high = mid - 1;
        }
        else
        {
            low = mid + 1; // look on the right
        }
    }
    return ans;
}

int main()
{
    vector<int> arr = {3, 5, 8, 15, 19};
    int ind = searchInsert(arr, 20);
    cout << ind << endl;

    return -1;
}

int binSearch(vector<int> &arr, int target)
{
    int low = 0;
    int high = arr.size() - 1; // index of last element.
    int index = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2; // middle elem index;

        if (arr[mid] >= target)
        {
            index =
            high = mid - 1; 
        }

        else if (arr[mid] > target)
        {
            // lies on the left hand side
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return index;
}
