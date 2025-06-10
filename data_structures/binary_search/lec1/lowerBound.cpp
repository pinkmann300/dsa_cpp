#include <iostream>
#include <cmath>

using namespace std;

int main();
int lowerBound(vector<int> arr, int lowerBound2);

int main()
{
    vector<int> arr = {3, 5, 8, 15, 19};
    int ind = lowerBound(arr, 9);
    cout << "Lower bound code implementation: " << ind << endl;
    return -1;
}

int lowerBound(vector<int> arr, int lowerBound2)
{
    int low = 0;
    int high = arr.size() - 1;
    int lowerBound3 = -1;

    while (low < high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] >= lowerBound2)
        {
            high = mid - 1;
            lowerBound3 = mid;
        }
        else
        {
            low = mid + 1;
        }
    }

    return lowerBound3;
}