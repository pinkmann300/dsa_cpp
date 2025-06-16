#include <iostream>
#include <cmath>
#include <numeric>
// Observations - could contain duplicates, in which case return lower bound.
using namespace std;

int binarySearch(vector<int> &values, int target);
bool binary2DSearch(vector<vector<int>> &matrix, int target);
int searchPosition(vector<int> &values, int target);

int main()
{
    return 0;
}

int binarySearch(vector<int> &values, int target)
{
    int found = -1;
    int low = 0;
    int high = values.size() - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (values[mid] == target)
        {
            found = mid;
            high = mid - 1;
        }
        else if (values[mid] > target)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return found;
}

bool binary2DSearch(vector<vector<int>> &matrix, int target)
{

    for (int i = 0; i < matrix.size(); i++)
    {
        int result = binarySearch(matrix[i], target);
        if (result != -1)
        {
            return true;
        }
    }

    return false;
}

int searchPosition(vector<int> &values, int target)
{
    int low = 0;
    int high = values.size() - 1;
    int targetIndex = m

        while (low <= high)
    {
        int mid = (low + high) / 2;
        if (values[mid] == target)
        {
            return mid;
        }

        if (values[mid] >= target)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return low;
}

