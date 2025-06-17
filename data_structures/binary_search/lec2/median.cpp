#include <iostream>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <vector>

using namespace std;

double median(vector<int> &arr1, vector<int> &arr2);

int main()
{
    vector<int> a = {1, 4, 7, 10, 12};
    vector<int> b = {2, 3, 6, 15};
    cout << "The median of two sorted array is " << (median(a, b)) << '\n';
    return -1;
}

double median(vector<int> &a, vector<int> &b)
{

    // Run it on the array which is of shorter length.
    if (a.size() > b.size())
    {
        return median(b, a);
    }

    int n1 = a.size();
    int n2 = b.size();

    int low = 0;
    int high = a.size();

    int leftLength = (a.size() + b.size() + 1) / 2;

    while (low <= high)
    {
        int mid1 = (low + high) / 2;
        int mid2 = leftLength - mid1;
        int l1 = INT_MIN;
        int l2 = INT_MIN;
        int r2 = INT_MAX;
        int r1 = INT_MAX;

        if (mid1 - 1 >= 0)
        {
            l1 = a[mid1 - 1];
        }

        if (mid2 - 1 >= 0)
        {
            l2 = b[mid2 - 1];
        }

        if (mid1 < n1)
        {
            r1 = a[mid1];
        }
        if (mid2 < n2)
        {
            r2 = b[mid2];
        }

        if (l1 <= r2 && l2 <= r1)
        {
            if ((n1 + n2) % 2 == 1)
            {
                return (max(l1, l2));
            }
            else
            {
                return ((double)(max(l1, l2)) + (double)(min(r1, r2))) / 2.0;
            }
        }

        else if (l2 > r1)
        {
            low = mid1 + 1;
        }
        else
        {
            high = mid1 - 1;
        }
    }

    return 0;
}