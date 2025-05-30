#include <iostream>
#include <cmath>

using namespace std;

int floorBinary(vector<int> &data1, int target);
int ceilBinary(vector<int> &data1, int target);

void findFloorAndCeil(vector<int> &data1, int target);

int main()
{
    vector<int> arr = {3, 4, 4, 7, 8, 10};
    int n = 6, x = 5;
    findFloorAndCeil(arr, 5);
    return -1;
}

int floorBinary(vector<int> &data1, int target)
{
    int low = 0;
    int high = data1.size() - 1;
    int ans = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (data1[mid] <= target)
        {
            ans = data1[mid];
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return ans;
}

int ceilBinary(vector<int> &data1, int target)
{
    int low = 0;
    int high = data1.size() - 1;

    int ceil = -1;

    while (low <= high)
    {
        int mid = (high + low) / 2;
        if (data1[mid] >= target)
        {
            ceil = data1[mid];
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return ceil;
}

void findFloorAndCeil(vector<int> &data1, int target)
{
    int f = floorBinary(data1, target);
    int c = ceilBinary(data1, target);

    cout << "Floor : " << f << endl;
    cout << "Ceil  : " << c << endl;
}