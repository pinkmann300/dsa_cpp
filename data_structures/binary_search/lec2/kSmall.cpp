#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>

using namespace std;

// Problem Statement: Given two sorted arrays of size m and n respectively, you are tasked with
// finding the element that would be at the kth position of the final sorted array.

int kthElement(vector<int> &a, vector<int> &b, int k);

int main()
{
    vector<int> a = {2, 3, 6, 7, 9};
    vector<int> b = {1, 4, 8, 10};
    cout << "The k-th element of two sorted array is: " << kthElement(a, b, 5) << '\n';
    return -1;
}

int kthElement(vector<int> &a, vector<int> &b, int k)
{
    if (a.size() > b.size())
    {
        return kthElement(b, a, k);
    }

    if (a.size() + b.size() < k)
    {
        return -1;
    }

    int low = max(0, k - a.size());
    int high = min(n, k);

    int leftLength = k;

    while (low <= high)
    {
        int mid1 = (low + high) / 2;
        int mid2 = leftLength - mid1;

        int l1 = INT_MIN;
        int l2 = INT_MIN;
        int r1 = INT_MAX;
        int r2 = INT_MAX;

        if (mid1 - 1 >= 0)
        {
            l1 = a[mid1 - 1];
        }

        if (mid2 - 1 >= 0)
        {
            l2 = b[mid2 - 1];
        }

        if (mid1 < a.size())
        {
            r1 = a[mid1];
        }

        if (mid2 < b.size())
        {
            r2 = b[mid2];
        }

        if (l1 <= r2 && l2 <= r1)
        {
            return max(l1, l2);
        }
        else if (l1 > r2)
        {
            high = mid1 - 1;
        }
        else
        {
            low = mid1 + 1;
        }
    }

    return 0;
}
