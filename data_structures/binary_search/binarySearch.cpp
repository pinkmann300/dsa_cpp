#include <iostream>
#include <cmath>

using namespace std;

int binarySearchIterative(vector<int> arr, int targetSum);
int binarySearchRecursive(vector<int> arr, int targetSum, int low, int high);

int main()
{
    vector<int> arr = {3, 4, 6, 7, 9, 12, 16, 17};
    cout << binarySearchIterative(arr, 6) << endl;
    cout << binarySearchRecursive(arr, 6, 0, arr.size() - 1) << endl;
    return -1;
}

int binarySearchIterative(vector<int> arr, int targetSum)
{
    int low = 0;
    int high = arr.size() - 1;

    bool found = false;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] == targetSum)
        {
            found = true;
            return mid;
        }
        else if (arr[mid] > targetSum)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return -1;
}

int binarySearchRecursive(vector<int> arr, int targetSum, int low, int high)
{
    if (low > high)
    {
        return -1;
    }

    int mid = (low + high) / 2;
    if (arr[mid] == targetSum)
    {
        return mid;
    }
    else if (arr[mid] > targetSum)
    {
        return binarySearchRecursive(arr, targetSum, low, mid - 1);
    }
    else
    {
        return binarySearchRecursive(arr, targetSum, mid + 1, high);
    }
}